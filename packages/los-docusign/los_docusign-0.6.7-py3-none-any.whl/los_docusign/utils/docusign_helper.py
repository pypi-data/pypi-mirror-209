#
# Created on Tue Dec 21 2021
#
# Copyright (c) 2021 Lenders Cooperative, a division of
# Summit Technology Group, Inc.
#
import base64
import hashlib
import hmac
import json
import logging
import re
from datetime import timedelta
from os import path
from xml.etree import cElementTree as ElementTree

from django.conf import settings
from django.http import Http404

# import sentry_sdk
from django.utils import timezone
from docusign_esign import ApiClient
from docusign_esign.client.api_exception import ApiException

from los_docusign.models import (
    DocusignEnvelopeStageData,
    DocusignOrgTemplate,
    DocuSignUserAuth,
)

from .XmlParser import XmlDictConfig

SCOPES = ["signature"]

LOGGER = logging.getLogger("root")


def get_webhook_is_json(default: bool | None = None):
    # `default` will allow other fn's to be able to accept input,
    #  and keep the same logic without repeated if statements everywhere this
    # is called
    if default is not None:
        return default
    # if nothing was passed in, check settings
    if hasattr(settings, "DOCUSIGN_ENABLE_JSON_SIM"):
        return settings.DOCUSIGN_ENABLE_JSON_SIM
    # if the setting is not found, fall back to xml
    return False


def get_docusign_user(organization_pk):
    try:
        # Try if the user is the available and has the docusign account
        docusign_user = DocuSignUserAuth.objects.get(
            organization_pk=organization_pk
        )
    except DocuSignUserAuth.DoesNotExist:
        # Else use the default user
        docusign_user = DocuSignUserAuth.objects.get(default_user=True)

    return docusign_user


def get_access_token(docusign_user, redirect_url=None):
    docusign_token_expiry = settings.DOCUSIGN_TOKEN_EXPIRY_IN_SECONDS

    if docusign_user.expires_at >= timezone.now():
        access_token = docusign_user.access_token
    else:
        token_response = _jwt_auth(
            docusign_user.docusign_api_username, redirect_url
        )
        try:
            if token_response["consent_url"]:
                return token_response
        except TypeError:
            pass
        access_token = token_response.access_token
        docusign_user.access_token = access_token
        docusign_user.expires_at = timezone.now() + timedelta(
            seconds=int(docusign_token_expiry)
        )
        docusign_user.save()

    return access_token


def check_docusign_access_token(organization_pk, redirect_uri=None):
    docusign_user = get_docusign_user(organization_pk)
    token_response = _jwt_auth(
        docusign_user.docusign_api_username, redirect_uri
    )
    LOGGER.info("Checking DocuSign Access Token")
    if token_response and isinstance(token_response, dict):
        # return the consent_url here
        return token_response
    return None


def _jwt_auth(docusign_api_username, redirect_uri):
    """JSON Web Token authorization"""
    api_client = ApiClient()
    api_client.set_base_path(settings.DOCUSIGN_AUTHORIZATION_SERVER)
    use_scopes = SCOPES
    if "impersonation" not in use_scopes:
        use_scopes.append("impersonation")

    # Catch IO error
    try:
        private_key = _get_private_key().encode("ascii").decode("utf-8")

    except (OSError, IOError):
        return "error"

    try:
        jwtTokenResponse = api_client.request_jwt_user_token(
            client_id=str(settings.DOCUSIGN_CLIENT_ID),
            user_id=docusign_api_username,
            oauth_host_name=str(settings.DOCUSIGN_AUTHORIZATION_SERVER),
            private_key_bytes=private_key,
            expires_in=3600,
            scopes=use_scopes,
        )
    except ApiException as err:
        body = err.body.decode("utf8")
        # Grand explicit consent for the application
        if "consent_required" in body:
            use_scopes = SCOPES
            if "impersonation" not in use_scopes:
                use_scopes.append("impersonation")
            consent_scopes = " ".join(use_scopes)
            if redirect_uri is None:
                redirect_uri = settings.DOCUSIGN_REDIRECT_APP_URL
            consent_url = (
                f"https://{settings.DOCUSIGN_AUTHORIZATION_SERVER}/oauth/auth?response_type=code&"
                f"scope={consent_scopes}&client_id={settings.DOCUSIGN_CLIENT_ID}&redirect_uri={redirect_uri}"
            )
            consent_url_dict = {}
            consent_url_dict["consent_url"] = consent_url
            return consent_url_dict
        else:
            LOGGER.error(
                f"Error while getting the jwt token for docusign: {err}"
            )
            raise

    return jwtTokenResponse


def _get_private_key():
    """
    Check that the private key present in the file and if it is, get it from
    the file.
    In the opposite way get it from config variable.
    """
    private_key_file = path.abspath(settings.DOCUSIGN_PRIVATE_KEY_FILE)
    if path.isfile(private_key_file):
        with open(private_key_file) as private_key_file:
            private_key = private_key_file.read()
    else:
        private_key = settings.DOCUSIGN_PRIVATE_KEY_FILE.encode().decode(
            "unicode-escape"
        )

    return private_key


def populate_text_tabs(text_tabs_forms, text_tabs_data: dict):
    # Need to populate all the text tabs with the values
    for textTabsInfo in text_tabs_forms:
        tab_label = textTabsInfo["tabLabel"]
        try:
            textTabsInfo["value"] = text_tabs_data.get(tab_label)
        except KeyError as e:
            LOGGER.debug(f"Key not found {e}")


def get_docusign_template(organization_pk, template_name=None):
    docusign_payload = None
    try:
        docusign_template = DocusignOrgTemplate.objects.get(
            organization_model="organization",
            docusign_template__template_type=template_name,
            organization_pk=organization_pk,
        ).docusign_template
    except DocusignOrgTemplate.DoesNotExist:
        dsua = DocuSignUserAuth.objects.get(default_user=True)
        docusign_template = DocusignOrgTemplate.objects.get(
            object_pk=dsua.object_pk,
            docusign_template__template_type=template_name,
        ).docusign_template

    docusign_payload = docusign_template.docusign_payload
    if docusign_payload is None:
        LOGGER.error(
            f"Payload Not found for org {organization_pk}. Check database..return"
        )
        return

    # resp = json.loads(docusign_payload)
    return docusign_payload


def _process_json_webhook_response(json_str):
    docusign_response_obj = json.loads(json_str)

    trimmed_object = {
        "raw": docusign_response_obj,
        "event": docusign_response_obj["event"],
        "envelope_id": docusign_response_obj["data"]["envelopeId"],
        "envelope_status": str(
            docusign_response_obj["data"]["envelopeSummary"]["status"]
        ).lower(),
        "custom_fields": {
            field["name"]: field["value"]
            for field in docusign_response_obj["data"]["envelopeSummary"][
                "customFields"
            ]["listCustomFields"]
        },
        "recipients": [],
    }

    for raw_recipient in (
        docusign_response_obj["data"]["envelopeSummary"]
        .get("recipients", {})
        .get("signers", [])
    ):
        recipient_data = {
            "recipient_id": raw_recipient["recipientId"],
            "email": raw_recipient["email"],
            "name": raw_recipient["name"],
            "sent_time": raw_recipient.get("sentDateTime", None),
            "routing_order": raw_recipient["routingOrder"],
            "custom_fields": raw_recipient.get("customFields"),
            "status": raw_recipient["status"],
        }

        if recipient_auth_status := raw_recipient.get(
            "RecipientAuthenticationStatus"
        ):
            phone_auth_status = recipient_auth_status.get("PhoneAuthResult", {})

            recipient_data["raw_auth_status"] = recipient_auth_status
            recipient_data["phone_auth_timestamp"] = phone_auth_status.get(
                "EventTimestamp"
            )

        # XXX: this is missing from the sample json
        # for rd_key, ras_key in (
        #     ('id_question_status',"IDQuestionsResult"),
        #     ('id_lookup_status',"IDLookupResult"),
        #     ('phone_auth_status',"PhoneAuthResult"),
        # ):
        #     status = recipient_auth_status.get(ras_key)
        #     if status is not None:
        #         status = str(status.get("Status")).lower()

        #     recipient_data[rd_key] = status

        trimmed_object["recipients"].append(recipient_data)

    # read and map documents
    document_pdfs = docusign_response_obj["data"]["envelopeSummary"].get(
        "envelopeDocuments", []
    )
    if not isinstance(document_pdfs, list):
        document_pdfs = [document_pdfs]

    documents = []
    for document_pdf in document_pdfs:
        document = {
            "name": document_pdf["name"],
            "pdf_bytes": document_pdf["PDFBytes"],
            "document_id": document_pdf.get("documentId"),
            "document_type": document_pdf["type"],
        }
        documents.append(document)

    trimmed_object["documents"] = documents

    return trimmed_object


def _process_xml_webhook_response(xml_string):
    root = ElementTree.XML(xml_string)
    request_data_dict = XmlDictConfig(root)
    m = re.search(
        "{http://www.docusign.net/API/(.+?)}EnvelopeStatus",
        str(request_data_dict),
    )
    api_version = None
    if m:
        api_version = m.group(1)
    else:
        # sentry_sdk.capture_exception(Exception(f'Failed to retrieve
        # API Version for the DocuSign Webhook: {str(request_data_dict)}'))
        raise Http404

    docusign_schema = f"{{http://www.docusign.net/API/{api_version}}}"

    # Since we are not using any of the data sent back by DocuSign, we
    # clear those fields which potentially causes json.dumps to fail to '
    # parse Decimal Values which are set by the Parser
    recipient_signers = request_data_dict[f"{docusign_schema}EnvelopeStatus"][
        f"{docusign_schema}RecipientStatuses"
    ][f"{docusign_schema}RecipientStatus"]

    if not isinstance(recipient_signers, list):
        recipient_signers = [recipient_signers]

    for recipients in recipient_signers:
        recipients[f"{docusign_schema}TabStatuses"] = None
        recipients[f"{docusign_schema}FormData"] = None

    line = re.sub(
        r"({http://www.docusign.net/API/[0-9].[0-9]})",
        "",
        json.dumps(request_data_dict),
    )
    docusign_response_obj = json.loads(line)

    trimmed_object = {
        "raw": docusign_response_obj,
        "envelope_id": docusign_response_obj["EnvelopeStatus"]["EnvelopeID"],
        "envelope_status": str(
            docusign_response_obj["EnvelopeStatus"]["Status"]
        ).lower(),
        "custom_fields": {
            docusign_response_obj["EnvelopeStatus"]["CustomFields"][field][
                "Name"
            ]: docusign_response_obj["EnvelopeStatus"]["CustomFields"][field][
                "Value"
            ]
            for field in docusign_response_obj["EnvelopeStatus"]["CustomFields"]
        },
        "recipients": [],
    }
    recipient_statues = docusign_response_obj["EnvelopeStatus"][
        "RecipientStatuses"
    ]
    for raw_recipient in recipient_statues:
        recipient_data = {
            "recipient_id": recipient_statues[raw_recipient]["RecipientId"],
            "email": recipient_statues[raw_recipient]["Email"],
            "name": recipient_statues[raw_recipient]["UserName"],
            "sent_time": recipient_statues[raw_recipient].get("Sent", None),
            "routing_order": recipient_statues[raw_recipient]["RoutingOrder"],
            "custom_fields": recipient_statues[raw_recipient].get(
                "CustomFields"
            ),
            "status": recipient_statues[raw_recipient]["Status"],
        }

        recipient_auth_status = recipient_statues[raw_recipient].get(
            "RecipientAuthenticationStatus", {}
        )
        phone_auth_status = (
            recipient_statues[raw_recipient]
            .get("RecipientAuthenticationStatus", {})
            .get("PhoneAuthResult", {})
        )

        recipient_data["raw_auth_status"] = recipient_auth_status
        recipient_data["phone_auth_timestamp"] = phone_auth_status.get(
            "EventTimestamp"
        )

        for rd_key, ras_key in (
            ("id_question_status", "IDQuestionsResult"),
            ("id_lookup_status", "IDLookupResult"),
            ("phone_auth_status", "PhoneAuthResult"),
        ):
            status = recipient_auth_status.get(ras_key)
            if status is not None:
                status = str(status.get("Status")).lower()

            recipient_data[rd_key] = status

        trimmed_object["recipients"].append(recipient_data)

    # read and map documents
    document_pdfs = docusign_response_obj["DocumentPDFs"]["DocumentPDF"]
    if not isinstance(document_pdfs, list):
        document_pdfs = [document_pdfs]

    documents = []
    for document_pdf in document_pdfs:
        document = {
            "name": document_pdf["Name"],
            "pdf_bytes": document_pdf["PDFBytes"],
            "document_id": document_pdf.get("DocumentID"),
            "document_type": document_pdf["DocumentType"],
        }
        documents.append(document)

    trimmed_object["documents"] = documents

    return trimmed_object


def process_webhook_response(xml_string, webhook_json_sim_enabled=None):
    if get_webhook_is_json(webhook_json_sim_enabled):
        docusign_data_dict = _process_json_webhook_response(xml_string)
    else:
        docusign_data_dict = _process_xml_webhook_response(xml_string)
    return docusign_data_dict


def process_docusign_webhook(
    xml_string,
    log_config,
    webhook_json_sim_enabled=None,
    event=None,
    event_type="WEBHOOK",
):
    docusign_data_dict = process_webhook_response(
        xml_string, webhook_json_sim_enabled
    )
    envelopeId = docusign_data_dict["envelope_id"]

    try:
        envelope_stage_data = DocusignEnvelopeStageData.objects.get(
            envelope_id=envelopeId
        )
    except DocusignEnvelopeStageData.DoesNotExist:
        LOGGER.error(f"Envelope id  {envelopeId} not found in system")
        raise Exception(f"Envelope id  {envelopeId} not found in system")

    return _extract_envelope_information(
        envelope_stage_data, docusign_data_dict, log_config, event_type
    )


def _extract_envelope_information(
    envelope_stage_data,
    docusign_data_dict,
    log_config=None,
    event_type="WEBHOOK",
):
    event_value = None
    try:
        envelope_id = docusign_data_dict["envelope_id"]
        recipients = docusign_data_dict["recipients"]
        envelope_status = str(docusign_data_dict["envelope_status"]).lower()

        if not isinstance(recipients, list):
            recipients = [recipients]

        recipient_failed_delivery = False
        recipient_failed_authentication = False
        recipients_data = []
        for recipient in recipients:
            recipient_data = {
                "recipient_id": recipient["recipient_id"],
                "email": recipient["email"],
                "name": recipient["name"],
                "sent_time": recipient["sent_time"],
                "routing_order": recipient["routing_order"],
                "custom_fields": recipient["custom_fields"],
                "status": recipient["status"],
            }

            recipient_auth_status = recipient.get("raw_auth_status")
            recipient_id_question_status = recipient.get("id_question_status")
            recipient_id_lookup_status = recipient.get("id_lookup_status")
            recipient_phone_auth_status = recipient.get("phone_auth_status")
            recipient_status = str(recipient_data["status"]).lower()

            recipient_data["phone_auth"] = {}

            if recipient_auth_status:
                phone_auth = {}
                current_status = envelope_stage_data.current_status

                if recipient_status in ["autoresponded"]:
                    recipient_failed_delivery = True
                if "failed" in (
                    recipient_id_lookup_status,
                    recipient_id_question_status,
                    recipient_phone_auth_status,
                ):
                    recipient_status = "authentication failed"
                    recipient_failed_authentication = True

                if current_status is None:
                    if recipient_phone_auth_status:
                        phone_auth = {
                            "status": recipient_phone_auth_status,
                            "last_event_time": recipient[
                                "phone_auth_timestamp"
                            ],
                            "fail_count": (
                                0
                                if recipient_phone_auth_status == "passed"
                                else 1
                            ),
                        }
                    recipient_data["phone_auth"] = phone_auth
                else:
                    current_status_recipients = current_status["recipients"]
                    for current_recipient in current_status_recipients:
                        phone_auth = current_recipient.get("phone_auth")
                        if (
                            current_recipient["email"]
                            == recipient_data["email"]
                            and current_recipient["name"]
                            == recipient_data["name"]
                            and current_recipient["custom_fields"][
                                "CustomField"
                            ]
                            in recipient_data["custom_fields"]
                        ):
                            # Currently not relying on the recipient id as we
                            # do store the sent recipient id and we receive
                            # the Docusign internal recipient id
                            if phone_auth is None:
                                phone_auth = {
                                    "fail_count": None,
                                    "status": None,
                                    "last_event_time": None,
                                }

                            if recipient_phone_auth_status:
                                if recipient_phone_auth_status == "passed":
                                    phone_auth["fail_count"] = 0
                                else:
                                    if phone_auth.get("fail_count"):
                                        phone_auth["fail_count"] += 1
                                    else:
                                        phone_auth["fail_count"] = 1
                                        phone_auth[
                                            "status"
                                        ] = recipient_phone_auth_status
                                        phone_auth[
                                            "last_event_time"
                                        ] = recipient["phone_auth_timestamp"]
                            recipient_data["phone_auth"] = phone_auth
                            break

            recipients_data.append(recipient_data)

        # Let's not overwrite the status of authentication failed if the
        # recipient failed authentication.
        # We need this to know if the receipient failed authentication and
        # later on completed the application
        # Assigning the envelope status value to recipient status as the for
        # multiple signers, Env status will be updated to "Completed" only
        # when all signers sign.

        if not envelope_stage_data.recipient_status == "authentication failed":
            envelope_stage_data.recipient_status = envelope_status

        if "failed" in (
            recipient_id_lookup_status,
            recipient_id_question_status,
            recipient_phone_auth_status,
        ):
            envelope_stage_data.recipient_status = "authentication failed"
            envelope_stage_data.recipient_auth_info = recipient_auth_status
            recipient_status = "authentication failed"

        if recipient_failed_authentication:
            recipient_status = "authentication failed"
        elif recipient_failed_delivery:
            recipient_status = "autoresponded"
        else:
            recipient_status = ""

        event_value = envelope_status

        if (
            recipient_status == "authentication failed"
            and envelope_status == "sent"
        ):
            event_value = "authentication failed"
        elif recipient_status == "autoresponded" and envelope_status == "sent":
            event_value = "autoresponded"

        if log_config:
            log_entry = log_config.get("model")(
                loan=log_config.get("loan"),
                object_pk=log_config.get("object_pk"),
                content_type=log_config.get("content_type"),
                requested_by=log_config.get("user"),
                request_url=log_config.get("request_url"),
                request_method=log_config.get("request_method"),
                request_headers=log_config.get("request_headers"),
                request_body=log_config.get("request_body"),
                request_time=log_config.get("timezone").now(),
                response_time=log_config.get("timezone").now(),
                tin=log_config.get("tin"),
                request_ip=log_config.get("request_ip"),
                response_code=log_config.get("response_code"),
                event_type=event_type,
                event=event_value,
            )
            log_entry.save()

        if event_value == "authentication failed":
            envelope_status = "authentication failed"

        envelope_output = {
            "envelopeId": envelope_id,
            "envelope_status": envelope_status,
            "recipients": recipients_data,
        }
        envelope_stage_data.envelope_status = envelope_status
        envelope_stage_data.current_status = envelope_output
        envelope_stage_data.recipient_status = recipient_status
        # envelope_stage_data.updated_at = timezone.now()
        envelope_stage_data.save()

        LOGGER.debug(f"END process_docusign_notification: {envelope_id}")

    except Exception as e:
        LOGGER.error(
            f"Exception while extracting status from Webhook notification: {e}"
        )
        if log_config:
            log_entry = log_config.get("model")(
                loan=log_config.get("loan"),
                object_pk=log_config.get("object_pk"),
                content_type=log_config.get("content_type"),
                requested_by=log_config.get("user"),
                request_url=log_config.get("request_url"),
                request_headers=log_config.get("request_headers"),
                request_body=log_config.get("request_body"),
                response_body=str(e),
                request_time=log_config.get("timezone").now(),
                response_time=log_config.get("timezone").now(),
                tin=log_config.get("tin"),
                request_ip=log_config.get("request_ip"),
                response_code=log_config.get("response_code"),
                event_type=event_type,
                event=event_value,
            )
            log_entry.save()
        raise Exception(
            "Exception while extracting status from Webhook notification!"
        ) from e
    return envelope_output


def ComputeHash(secret, payload):
    hashBytes = hmac.new(secret, msg=payload, digestmod=hashlib.sha256).digest()
    base64Hash = base64.b64encode(hashBytes)
    return base64Hash


def HashIsValid(secret, payload, verify):
    return hmac.compare_digest(verify, ComputeHash(secret, payload))


def validate_received_webhook(secret, payload, verify):
    return HashIsValid(
        secret=secret.encode(), payload=payload, verify=verify.encode()
    )

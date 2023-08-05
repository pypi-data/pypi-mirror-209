#
# Created on Tue Dec 21 2021
#
# Copyright (c) 2021 Lenders Cooperative, a division of Summit Technology Group, Inc.
#
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.shortcuts import redirect

from .models import (
    DocusignChoiceConfig,
    DocusignEnvelopeStageData,
    DocusignOrgTemplate,
    DocusignTemplate,
    DocusignTemplateOrgExclusion,
    DocuSignUserAuth,
)

# from loans.models import EtranLoan
from .utils.docusign_helper import check_docusign_access_token


@admin.register(DocusignEnvelopeStageData)
class DocusignEnvelopeStageDataAdmin(admin.ModelAdmin):
    model = DocusignEnvelopeStageData
    list_display = (
        "id",
        "envelope_id",
        "object_pk",
        "record_status",
        "recipient_status",
        "created",
        "modified",
    )
    search_fields = ("envelope_id", "object_pk")
    readonly_fields = ["content_type", "docusign_user"]

    def get_actions(self, request):
        # Disable delete
        actions = super(DocusignEnvelopeStageDataAdmin, self).get_actions(
            request
        )
        return actions

    actions = ["clear_docusign_throttling_locks", "clear_docusign_app_locks"]

    def clear_docusign_throttling_locks(self, request, queryset):
        rate_reset_lock = cache.delete("docusign_rate_reset")
        self.message_user(
            request, f"DocuSign Throttling Lock Released: {rate_reset_lock}"
        )

    clear_docusign_throttling_locks.short_description = (
        "Clear Docusign Throttling Lock"
    )

    def clear_docusign_app_locks(self, request, queryset):
        delete_count = 0
        for envelope in queryset.all():
            envlope_obj = DocusignEnvelopeStageData.objects.get(
                envelope_id=envelope
            )
            if cache.delete(f"send_for_docusign:{envlope_obj.object_pk}"):
                delete_count += 1
        self.message_user(
            request,
            f"{delete_count} successfully released redis locks on applications for docusign.",
        )

    clear_docusign_app_locks.short_description = (
        "Clear Docusign Application Lock"
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(DocusignOrgTemplate)
class DocusignOrgTemplateAdmin(admin.ModelAdmin):
    model = DocusignOrgTemplate
    list_display = (
        "organization_model",
        "docusign_template",
        "created",
        "modified",
    )
    readonly_fields = ["organization_model", "docusign_template"]
    list_filter = (
        "organization_model",
        "docusign_template",
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(DocusignChoiceConfig)
class DocusignChoiceConfigAdmin(admin.ModelAdmin):
    model = DocusignChoiceConfig
    list_display = ("docusign_model", "config_key", "created", "modified")
    # autocomplete_fields = ["organization_model"]
    list_filter = (
        "docusign_model",
        "config_key",
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(DocusignTemplate)
class DocusignTemplateAdmin(admin.ModelAdmin):
    model = DocusignTemplate
    list_display = (
        "template_type",
        "is_active",
        "created",
        "modified",
    )
    list_filter = ("template_type",)
    readonly_fields = ["template_type"]

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(DocusignTemplateOrgExclusion)
class DocusignTemplateOrgExclusionAdmin(admin.ModelAdmin):
    model = DocusignTemplateOrgExclusion
    list_display = (
        "organization_model",
        "document_name",
        "template",
        "created",
        "modified",
    )
    list_filter = ("organization_model", "template")
    readonly_fields = ["organization_model", "document_name", "template"]

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    model = ContentType

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(DocuSignUserAuth)
class DocuSignUserAuthAdmin(admin.ModelAdmin):
    model = DocuSignUserAuth
    list_display = ("organization_model", "default_user", "created", "modified")
    readonly_fields = ["organization_model"]
    # list_filter = ('organization_model',)

    def check_docusign_consent(self, request, queryset):
        for org in queryset:
            # loan = EtranLoan.objects.filter(organization_id=org.id).last()
            consent_url = check_docusign_access_token(org)
            if consent_url.get("consent_url", None):
                print(f"Consent URL: {consent_url}")
                print(f"Current Path: {request.get_full_path()}")
                # /admin/
                request.session[
                    "docusign_redirect_path"
                ] = request.get_full_path()
                BASE_URL = settings.BASE_URL
                DOCUSIGN_REDIRECT_APP_URL = settings.DOCUSIGN_REDIRECT_APP_URL
                redirect_uri = BASE_URL + "/docusign_redirect"
                final_consent_url = consent_url["consent_url"].replace(
                    DOCUSIGN_REDIRECT_APP_URL, redirect_uri
                )
                print(f"Final Consent URL: {final_consent_url}")
                return redirect(final_consent_url)

    check_docusign_consent.short_description = (
        "Check if consent is required from Docusign"
    )

    def get_actions(self, request):
        # Disable delete
        actions = super(DocuSignUserAuthAdmin, self).get_actions(request)
        return actions

    actions = [check_docusign_consent]

    # def has_delete_permission(self, request, obj=None):
    #     return False

from django.contrib import admin
from .models import (
    HeroSection,
    Feature,
    FrequentlyAskedQuestion,
    ProcessStep,
    AboutSection,
    Service,
    Package,
    Payment,
    Sender,
    Recipient,
    TrackingUpdate,
)


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ("position", "title", "icon_class")
    fields = ("position", "title", "description", "icon_class")
    ordering = ("position",)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", "description", "image")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")
    fields = ("title", "description", "icon_class")


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ("question",)


class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 1
    max_num = 1
    classes = ["collapse"]


class SenderInline(admin.StackedInline):
    model = Sender
    extra = 1
    max_num = 1
    classes = ["collapse"]


class RecipientInline(admin.StackedInline):
    model = Recipient
    extra = 1
    max_num = 1
    classes = ["collapse"]


class TrackingUpdateInline(admin.TabularInline):
    model = TrackingUpdate
    extra = 1
    readonly_fields = ["timestamp"]


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "tracking_number",
        "current_status",
        "shipment_type",
        "estimated_delivery_date",
        "created_at",
    )
    list_filter = (
        "current_status",
        "shipment_type",
        "return_status",
        "created_at",
    )
    search_fields = (
        "tracking_number",
        "point_of_departure",
        "receiving_address",
        "courier_personnel",
    )
    inlines = [
        SenderInline,
        RecipientInline,
        PaymentInline,
        TrackingUpdateInline,
    ]

    fieldsets = (
        (
            "BASIC INFORMATION",
            {
                "fields": (
                    "title",
                    "image",
                    "description",
                ),
            },
        ),
        (
            "DELIVERY INFORMATION",
            {
                "fields": (
                    "current_status",
                    "shipment_type",
                    "point_of_departure",
                    "receiving_address",
                    "estimated_delivery_date",
                ),
            },
        ),
        (
            "PACKAGE DETAILS",
            {
                "classes": ("collapse",),
                "fields": (
                    "weight",
                    "dimensions",
                    "special_instructions",
                ),
            },
        ),
        (
            "RETURN INFORMATION",
            {
                "classes": ("collapse",),
                "fields": (
                    "return_status",
                    "return_instructions",
                ),
            },
        ),
    )
    readonly_fields = (
        "package_uuid",
        "tracking_number",
    )

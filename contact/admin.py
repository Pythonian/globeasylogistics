from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Information, Message


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = [
            "footer_info",
            "email",
            "address",
            "phone_number",
            "office_hours",
            "facebook_url",
            "instagram_url",
            "twitter_url",
        ]

    def clean(self):
        if Information.objects.exists() and not self.instance.pk:
            raise ValidationError("Only one Information instance is allowed.")
        return super().clean()


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    form = InformationForm
    list_display = ("email", "phone_number")

    def has_add_permission(self, request):
        # Prevent adding more than one instance
        if Information.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email")
    search_fields = ("subject", "name", "email")
    list_filter = ["created"]

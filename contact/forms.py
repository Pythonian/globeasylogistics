from django import forms

from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your full name"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your email address"}
            ),
            "subject": forms.TextInput(
                attrs={"placeholder": "Enter the subject of your message"}
            ),
            "body": forms.Textarea(attrs={"placeholder": "Write your message here"}),
        }

import json
import logging
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

from config.utils import send_email_thread
from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact(request):
    form = ContactForm()

    template = "contact/form.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@csrf_protect
def send_contact_form(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = ContactForm(data)

            if form.is_valid():
                _ = form.save()

                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                subject = form.cleaned_data["subject"]
                body = form.cleaned_data["body"]
                current_year = datetime.now().year

                context = {
                    "subject": subject,
                    "name": name,
                    "email": email,
                    "body": body,
                    "current_year": current_year,
                }

                # Render email templates
                html_content = render_to_string(
                    "contact/emails/contact_email.html",
                    context,
                )
                text_content = render_to_string(
                    "contact/emails/contact_email.txt",
                    context,
                )

                email_subject = f"Contact Form: {subject}"
                recipient = settings.DEFAULT_FROM_EMAIL
                # TODO: reply_to = [email]

                send_email_thread(
                    email_subject,
                    text_content,
                    html_content,
                    recipient,
                )

                return JsonResponse({"status": "success"}, status=200)
            else:
                # Return form errors
                return JsonResponse(
                    {"status": "error", "errors": form.errors},
                    status=400,
                )

        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON data."},
                status=400,
            )
        except Exception as e:
            logger.exception(f"Unexpected error occured: {str(e)}")
            return JsonResponse(
                {
                    "status": "error",
                    "message": "An unexpected error occurred.",
                },
                status=500,
            )

    return JsonResponse({"status": "invalid method"}, status=400)

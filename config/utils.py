import logging
import threading
from mailjet_rest import Client
from django.conf import settings


logger = logging.getLogger(__name__)


def send_email_via_mailjet(
    subject,
    text_content,
    html_content,
    recipient_email,
    recipient_name=None,
    reply_to=None,
):
    try:
        mailjet = Client(
            auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY),
            version="v3.1",
        )

        sender = {
            "Email": settings.DEFAULT_FROM_EMAIL,
            "Name": settings.MAILJET_SENDER_NAME,
        }

        recipient = {
            "Email": recipient_email,
            "Name": recipient_name if recipient_name else recipient_email.split("@")[0],
        }

        headers = {}
        if reply_to:
            headers["Reply-To"] = reply_to

        data = {
            "Messages": [
                {
                    "From": sender,
                    "To": [recipient],
                    "Subject": subject,
                    "TextPart": text_content,
                    "HTMLPart": html_content,
                    "Headers": headers,
                }
            ]
        }

        result = mailjet.send.create(data=data)
        if result.status_code != 200:
            logger.error(
                f"Failed to send email to {recipient_email}: {result.status_code} {result.json()}"
            )
        else:
            logger.info(
                f"Email sent successfully to {recipient_email}: {result.status_code}"
            )
    except Exception as e:
        logger.exception(
            f"An error occurred while sending email to {recipient_email}: {str(e)}"
        )


def send_email_thread(
    subject,
    text_content,
    html_content,
    recipient_email,
    recipient_name=None,
    reply_to=None,
):
    email_thread = threading.Thread(
        target=send_email_via_mailjet,
        args=(
            subject,
            text_content,
            html_content,
            recipient_email,
            recipient_name,
            reply_to,
        ),
    )
    email_thread.start()

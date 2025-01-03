from django.urls import path

from .views import contact, send_contact_form

app_name = "contact"

urlpatterns = [
    path("send-contact/", send_contact_form, name="send_contact_form"),
    path("", contact, name="form"),
]

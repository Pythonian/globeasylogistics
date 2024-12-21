from django.urls import path

from .views import home, about, services, track, contact

urlpatterns = [
    path("contact/", contact, name="contact"),
    path("track/", track, name="track"),
    path("services/", services, name="services"),
    path("about/", about, name="about"),
    path("", home, name="home"),
]

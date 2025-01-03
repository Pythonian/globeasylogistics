from django.urls import path

from .views import home, about, services, track

urlpatterns = [
    path("track/", track, name="track"),
    path("services/", services, name="services"),
    path("about/", about, name="about"),
    path("", home, name="home"),
]

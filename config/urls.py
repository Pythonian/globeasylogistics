from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("contact.urls", namespace="contact")),
    path("", include("packages.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

admin.site.site_header = "GlobEasyLogistics Admin"
admin.site.index_title = "GlobEasyLogistics Admin"
admin.site.site_title = "GlobEasyLogistics Administration"

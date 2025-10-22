"""
URL Configuration for Auth project.

This module contains the root URL configuration for the Auth project, including:
- Admin interface URLs (/admin/)
- Core app URLs under /accounts/ namespace
- Static/Media file serving in debug mode
- Browser reload URLs in debug mode

Debug-only URLs:
    - Static files served from settings.STATIC_ROOT
    - Media files served from settings.MEDIA_ROOT
    - Browser reload endpoint at /__reload__/

For more information on Django URL configuration, see:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home"),
    path("accounts/", include(("core.urls", "core"), namespace="accounts")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # type: ignore
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls")),]

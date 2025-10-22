"""
URL configuration for the core app.

This module defines URL patterns for user authentication and dashboard access.
All URLs are namespaced under 'accounts:' in the main URLconf.

URL Patterns:
    - /: Signup page for new user registration
    - /login/: User login page
    - /logout/: Handles user logout
    - /dashboard/: User dashboard (requires authentication)
        Shows different views for doctors and patients

Usage:
    Use the 'accounts' namespace when reversing these URLs, e.g.:
    {% url 'accounts:login' %}
    {% url 'accounts:dashboard' %}
"""

from django.urls import path
from .views import login_view, signup_view, dashboard_view, logout_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
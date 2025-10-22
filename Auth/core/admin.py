"""
Admin configuration for core app.

This module registers the core app's models with Django's admin interface,
making them accessible and manageable through the admin panel at /admin/.

Registered models:
    - UserProfile: Extended user profile model with additional fields
      like profile picture, address, and doctor status
"""

from django.contrib import admin
from .models import UserProfile


admin.site.register(UserProfile)

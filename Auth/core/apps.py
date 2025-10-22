"""
Core app configuration module.

This module defines the Django application configuration for the core app,
which handles user authentication, profiles, and dashboard functionality.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuration class for the core application.
    
    Attributes:
        default_auto_field (str): Specifies BigAutoField as the primary key type
            for models that don't explicitly define a primary key.
        name (str): The name of the application package.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

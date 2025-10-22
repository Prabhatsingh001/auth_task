"""
WSGI config for Auth project.

This module contains the WSGI application configuration for the Auth project.
It exposes the WSGI callable as a module-level variable named 'application'.

The application variable is used by WSGI servers (like Gunicorn, uWSGI) to
serve the Django application in a production environment.

For more information on this file, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Auth.settings')

application = get_wsgi_application()

"""
WSGI config.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

DJANGO_SETTINGS_MODULE = ''

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

from django.core.wsgi import get_wsgi_application  # isort:skip

application = get_wsgi_application()

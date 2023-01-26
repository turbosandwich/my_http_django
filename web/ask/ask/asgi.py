"""

ASGI config - "ask" project.

It -> ASGI callable as module-level variable "application"

For more information: https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/


"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ask.settings')

application = get_asgi_application()



"""
WSGI config for BuTianBug project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
from os.path import join, dirname, abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))  # 3
import sys  # 4

sys.path.insert(0, PROJECT_DIR)  # 5

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BuTianBug.settings")

application = get_wsgi_application()

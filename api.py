import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_mentor.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
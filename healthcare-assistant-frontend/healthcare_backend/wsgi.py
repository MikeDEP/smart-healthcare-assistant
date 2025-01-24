# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_backend.settings')  # replace 'myproject' with your actual project name
application = get_wsgi_application()

import os
import sys

from django.core.management import execute_from_command_line
from django.shortcuts import render
from django.urls import path


# Django settings are in this file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)

# Settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_HOSTS = ["*"]
DEBUG = True
SECRET_KEY = "Pw7k~s!oK&X@i{<AAo>pG)Z}Z`Cn$VZ*9{H)TP+78k^eI^(k:5"
INSTALLED_APPS = [
    "django.contrib.staticfiles",  # serve static files with dev server
]

# URL conf is in this file
ROOT_URLCONF = __name__

# Templates are located in ./static/
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
    }
]

# Static URL is /static/; static files are in [BASE_DIR]/static/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# Views
def home(request):
    context = dict(title="Home")
    return render(request, "home.html", context=context)


# URLs
urlpatterns = [
    path("", home, name="home"),
]

# Run with "python app.py runserver"
execute_from_command_line(sys.argv)

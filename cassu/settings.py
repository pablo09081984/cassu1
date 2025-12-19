import os
from pathlib import Path

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]

BASE_DIR = Path(__file__).resolve().parent.parent  # CASSU\


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # ✅ obligatorio
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # opcional: [BASE_DIR / "templates"]
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]



DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "cassu" / "static"]

ROOT_URLCONF = "cassu.urls"
WSGI_APPLICATION = "cassu.wsgi.application"

SECRET_KEY = "django-insecure-cassu-1234567890"  # cualquier string NO vacío
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]




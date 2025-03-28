"""
Django settings for statisticpro project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4(t0h4yye4e@p)ia5512h&9wbo!7-e*0h4j&##$(i)in#mmq2r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
"a837-2601-646-9e00-2720-711f-5abd-261c-fdc3.ngrok-free.app",
"127.0.0.1",
"localhost",
]

CSRF_TRUSTED_ORIGINS = [
"https://a837-2601-646-9e00-2720-711f-5abd-261c-fdc3.ngrok-free.app"
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'statapp',
    'corsheaders',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    
]

# Allow frontend to access the backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",# Vite React URL
    'https://a837-2601-646-9e00-2720-711f-5abd-261c-fdc3.ngrok-free.app',  
    'http://127.0.0.1:8000',
    "http://localhost:3000",
    'http://127.0.0.1:8001',
    "http://localhost:3001",
]
 
# If using credentials like JWT
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
# CORS_ALLOW_HEADERS = ["authorization", "content-type"]

ROOT_URLCONF = "statisticpro.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "statisticpro.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",  # Use MySQL backend
#         "NAME": os.getenv('MYSQL_DATABASE', 'django_db'),  # Replace with your database name
#         "USER": "root",  # Replace with your MySQL username
#         "PASSWORD": os.getenv('MYSQL_ROOT_PASSWORD', 'Momo@7002'),  # Replace with your MySQL password
#         "HOST": os.getenv('MYSQL_HOST', 'localhost'),  # Since you're using a local database
#         "PORT": "3306",  # Default MySQL port
#         "OPTIONS": {
#             "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
#              'unix_socket': '',
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

"""
Django settings for pylabber project.

Generated by 'django-admin startproject' using Django 2.1a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
import os

from django_mri.analysis.interfaces import interfaces


env = environ.Env(
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(list, ["*"]),
    SECRET_KEY=(str, "asdf5sag231sd$#%SADF2341a"),
    DB_NAME=(str, "pylabber"),
    DB_USER=(str, "postgres"),
    DB_PASSWORD=(str, ""),
    DB_HOST=(str, "localhost"),
    DB_PORT=(int, 5432),
    RAW_SUBJECT_TABLE_PATH=(str, "subjects.xlsx"),
)
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd Party
    "django_extensions",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "corsheaders",
    # Extensions
    "django_dicom",
    "django_mri",
    "django_analysis",
    # Local
    "research",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pylabber.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ]
        },
    }
]

WSGI_APPLICATION = "pylabber.wsgi.application"

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

AUTH_USER_MODEL = "accounts.User"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
SIMILARITY_VALIDATOR = (
    "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
)

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": SIMILARITY_VALIDATOR},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "pylabber.views.pagination.StandardResultsSetPagination",
    "PAGE_SIZE": 20,
    # djangorestframework-camel-case settings
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
}
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "accounts.serializers.UserSerializer"
}


CORS_ORIGIN_WHITELIST = [
    "https://www.pylabber.org",
    "https://pylabber.org",
    "http://localhost:8080",
]


# pylabber configuration
SUBJECT_MODEL = "research.Subject"
STUDY_GROUP_MODEL = "research.Group"
RAW_SUBJECT_TABLE_PATH = env("RAW_SUBJECT_TABLE_PATH")

# django_analysis_configuration
ANALYSIS_INTERFACES = interfaces
ANALYSIS_BASE_PATH = os.path.join(MEDIA_ROOT, "analysis")

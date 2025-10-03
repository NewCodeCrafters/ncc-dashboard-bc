import os

from .base import *

from dotenv import load_dotenv

load_dotenv()

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("SQL_DATABASE"),
        "USER": os.getenv("SQL_USER"),
        "PASSWORD": os.getenv("SQL_PASSWORD"),
        "HOST": os.getenv("SQL_HOST", "localhost"),
        "PORT": os.getenv("SQL_PORT", "5432"),
        # "OPTIONS": {
        #     "sslmode": "require",
        #     "sslrootcert": "global-bundle.pem",  # Path to your RDS CA certificate
        # },
    }
}

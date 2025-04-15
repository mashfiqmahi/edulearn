from mysite.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
CSRF_TRUSTED_ORIGINS = ['https://web-production-5068.up.railway.app']

DATABASE = {
    'ENGINE':'django.db.backends.postgresql_psycopg2',
    'NAME': config('DATABASE_NAME'),
    'USER': config('DATABASE_USER'),
    'PASSWORD': config('DATABASE_PASSWORD'),
    'HOST': config('DATABASE_HOST'),
    'PORT': config('DATABASE_PORT'),
    'OPTIONS': {'sslmode':'require'},
}
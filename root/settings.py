"""
Django settings for emlauncher project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import environ

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, '*$+179-==kwp76$q2o684nz+0zkjtvk4t2k2m4+gk$$kdy4zk='),
    DATABASE_URL=(str, 'postgresql://root:password@localhost:18688/db'),
    REDIS_URL=(str, 'redis://localhost:18689/2'),
    CACHE_URL=(str, 'rediscache://localhost:18689/0?client_class=django_redis.client.DefaultClient'),
    CELERY_BROKER_URL=(str, 'redis://localhost:18689/1'),
    CHANNEL_REDIS_HOST=(str, 'localhost'),
    CHANNEL_REDIS_PORT=(str, '18689'),
    DEFAULT_FROM_EMAIL=(str, 'info@inspectorio.com'),
    SENTRY_DSN=(str, ''),
    ALLOWED_HOSTS=(str, '*'),
    EMAIL_URL=(str, 'smtp://localhost:25'),
    CORS_ORIGIN_WHITELIST=(str, '*'),
    INTERNAL_IPS=(str, '127.0.0.1'),
)

environ.Env.read_env('.env_custom')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
root = environ.Path(__file__) - 2  # 2 level above
BASE_DIR = root()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS_CONFIG = env('ALLOWED_HOSTS')  # type: str
if ALLOWED_HOSTS_CONFIG:
    ALLOWED_HOSTS = ALLOWED_HOSTS_CONFIG.split(',')
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'channels',

    'accounts',
    'esp8266',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'
ASGI_APPLICATION = "root.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(env('CHANNEL_REDIS_HOST'), int(env('CHANNEL_REDIS_PORT')))],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'accounts.User'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://github.com/pmclanahan/django-celery-email
vars().update(env.email(backend='djcelery_email.backends.CeleryEmailBackend'))
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = root('staticfiles')
STATICFILES_DIRS = (
    root('static'),
)

# https://docs.sentry.io/clients/python/integrations/django/
RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN'),
}

# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
CELERY_BROKER_URL = env('CELERY_BROKER_URL')

INTERNAL_IPS = env('INTERNAL_IPS').split(',')  # type: list

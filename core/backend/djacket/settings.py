"""
Django settings for djacket project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Front-end folder to keep views, styles and scripts.
# Default is set to a BASE_DIR/../'frontend'
FRONTEND_DIR = os.path.join(BASE_DIR, '..', 'frontend')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'a randomly generated string will be installed'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# For security reasons, set domain or host of your site in ALLOWED_HOSTS
#   e.g.
#       ALLOWED_HOSTS = ['.exampledomain.com']
# You can find more details in https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts.


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_pjax',
    'user',
    'repository',
    'filter'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djacket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(FRONTEND_DIR, 'public', 'build', 'views'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'djacket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Currently there's not much of a database transaction (only on user/repository creation)
#   so SQLite database would suffice. But in case you feel it's not enough for you
#   comment sqlite3 database settings below and uncomment PostgreSQL settings.
#   Make sure your PostgreSQL database is setup first and your database is created.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, '..', 'djacketdb.sqlite3'),
    }
}

# PostgreSQL database settings.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'djacket',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# Static files will be collected to be served in 'BASE_DIR/../static/', outside of server code.

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'public', 'build', 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Media files (User avatar images)
# Default is set to ''BASE_DIR/../media', outside of server code.

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'


# User authentication urls configuration.

LOGIN_URL = 'index'
LOGOUT_URL = 'user_logout'
LOGIN_REDIRECT_URL = 'index'


# Djacket version number and site name.

DJACKET_VERSION = '0.1.0'
SITE_NAME = 'Djacket'


# Git repositories deposit folder on server.
# This folder can be set by initializing a variable called 'GIT_DEPOSIT_ROOT'.
#   e.g.
#       GIT_DEPOSIT_ROOT = '/path/to/your/deposit/folder'
# Other variables from installation such as ALLOWED_HOSTS and SECRET_KEY will be set here.
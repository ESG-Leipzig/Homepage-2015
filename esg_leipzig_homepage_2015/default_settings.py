"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'esg_leipzig_homepage_2015',
    'esg_leipzig_newsletter_2015',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'esg_leipzig_homepage_2015.middlewares.LinkToFlatPageMiddleware',
)

ROOT_URLCONF = 'esg_leipzig_homepage_2015.urls'

WSGI_APPLICATION = ''

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de'

LANGUAGES = (
    ('de', ugettext_lazy('Deutsch')),
    ('en', ugettext_lazy('Englisch')),
)

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bower_components'),
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')


# Miscellaneous entries

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'esg_leipzig_homepage_2015.context_processors.flatpages',
)

FORMAT_MODULE_PATH = 'esg_leipzig_homepage_2015.formats'

# Used in views.HomeView to decide how many minutes events are shown after
# beginning.
EVENT_DELAY_IN_MINUTES = 180


# Email settings

EMAIL_NEWSLETTER_FROM_MAIL = 'newsletter@esg-leipzig.de'

EMAIL_SUBJECT_PREFIX = '[ESG Homepage] '

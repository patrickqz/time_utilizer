"""
Django settings for time_utilizer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

FACEBOOK_APP_ID = '702764503137707'
FACEBOOK_SECRET_KEY = '02bb84389b9f666f0edaac232f166acf'

# Optionally set default permissions to request, e.g: ['email', 'user_about_me']
FACEBOOK_SCOPE = []

# And for local debugging, use one of the debug middlewares and set:
# FACEBOOK_DEBUG_TOKEN = ''
# FACEBOOK_DEBUG_UID = ''
# FACEBOOK_DEBUG_COOKIE = ''
# FACEBOOK_DEBUG_SIGNEDREQ = ''

# Optionally throw exceptions instead of returning HTTP errors on signed request issues
FACEBOOK_RAISE_SR_EXCEPTIONS = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cb9qnj&%g2x$htegv&dyp%@pb^gyj&^tqtv%wf5w!&tmn@g&+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_facebook',
    'utilizer',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_facebook.middleware.FacebookMiddleware'
)

ROOT_URLCONF = 'time_utilizer.urls'

WSGI_APPLICATION = 'time_utilizer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timeutilizer',
        'USER': 'postgres',
        'PASSWORD': 'pinacolada',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

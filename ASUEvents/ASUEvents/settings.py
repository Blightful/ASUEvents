"""
Django settings for ASUEvents project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')aba8(f$sf=o%z=+0kyl%e2_fo0o#18#=i$6ws&r)th1c!key&'

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
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ASUEvents.urls'

WSGI_APPLICATION = 'ASUEvents.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

# Media
MEDIA_URL = '/media/'
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

# Project Templates
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

ASSETS_URL = os.path.join(STATIC_URL, 'assets/')
ASSETS_PATH = os.path.join(STATIC_PATH, 'assets')

ASSETS_GLOBAL = os.path.join(ASSETS_URL, 'global/')
ASSETS_ADMIN = os.path.join(ASSETS_URL, 'admin/')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.tz',
    'home.context.context_fonts',
    'home.context.context_styles',
    'home.context.context_scripts',
)


PLUGINS_URL = os.path.join(ASSETS_URL, 'global', 'plugins/')
PLUGINS_PATH = os.path.join(ASSETS_PATH, 'global', 'plugins')
PLUGINS_CORE = (
    'jquery.min.js',
    'jquery-migrate.min.js',
    'jquery-ui/jquery-ui.min.js',
    'bootstrap/js/bootstrap.min.js',
    'bootstrap-hover-dropdown/bootstrap-hover-dropdown.min.js',
    'jquery-slimscroll/jquery.slimscroll.min.js',
    'jquery.blockui.min.js',
    'jquery.cokie.min.js',
    'uniform/jquery.uniform.min.js',
    'bootstrap-switch/js/bootstrap-switch.min.js',
)

STYLES_CORE = (
    'font-awesome/css/font-awesome.min.css',
    'simple-line-icons/simple-line-icons.min.css',
    'bootstrap/css/bootstrap.min.css',
    'uniform/css/uniform.default.css',
    'bootstrap-switch/css/bootstrap-switch.min.css',
)
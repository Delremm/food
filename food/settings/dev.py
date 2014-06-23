from food.settings.common import *

DEBUG = True


MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static/media'))
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += (
    # If you're using Django 1.7.x or later
    #'debug_toolbar.apps.DebugToolbarConfig',
    # If you're using Django 1.6.x or earlier
    'debug_toolbar',
)

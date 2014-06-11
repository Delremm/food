"""
Django settings for food project.

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
SECRET_KEY = 'xq-(yferz3dlmo^eru3cs*ak&!v%u6nyhu30hd4c#h(#)m-_5a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'extended_flatpages',
    'sitemetrics',
    'flatblocks',
    'rest_framework',
    'mptt',
    'django.contrib.webdesign',
    "djrill",
    'south',
    'emailer',
    "easy_thumbnails",
    "filer",
    'frontend',
    'food_app',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "frontend.context_processors.general_context")

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'food.urls'

WSGI_APPLICATION = 'food.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_URL    = '/media/'
STATIC_URL = '/static/'

SITE_CONTEXT = {}
SITE_CONTEXT['default_title'] = 'Мудрый обед'


# "djrill" EMAILS   mandrillapp.com
MANDRILL_API_KEY = "Mnq6I1CFVEpbNKxRe9Xshw"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}


SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

#apps settings

FORMEAL_CONF = {
    'MACRO': {
        'ACTIVITIES': [
            # {'id': 1, 'name': u"бездействие", 'mul': 1.2,
            #     'description': u'нет физической активности, напрмер, парализованный пациент'},
            {'id': 1, 'name': "сидячий образ жизни", 'mul': 1.30,
                'description': 'офисный работник, не занимающийся спортом'},
            {'id': 2, 'name': "легкая активность", 'mul': 1.375,
                'description': 'офисный работник, занимающийся спортом 1-3 раза в неделю'},
            {'id': 3, 'name': "умеренная активность", 'mul': 1.55,
                'description':
                    'офисный работник, занимающийся спортом 3-5 раз в неделю или рабочий, заримающийся 1-3 раза в неделю'},
            {'id': 4, 'name': "высокая активность", 'mul': 1.75,
                'description': 'занимающийся тяжелым физическим трудом или офисный работник, профессионально занимающийся спортом 6-7 раз в неделю'},
            {'id': 5, 'name': "сверхвысокая активность", 'mul': 1.8,
                'description': 'занимающийся тяжелым физическим трудом работник, занимающийся спортом 3-5 раз в неделю'},        ],
    },
}

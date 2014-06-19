from food.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['.wisemeal.ru']

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'food_media'))
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'food_static'))

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'food',
        'USER': 'food_admin',
        'PASSWORD': 'food_admin21',
        'PORT': '3306',
        'HOST': '127.0.0.1'
    }
}

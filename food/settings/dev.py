from food.settings.common import *

DEBUG = True

# Paths
#MEDIA_ROOT   = ROOT_DIR + '/web/media/'
MEDIA_URL    = '/media/'        # Must end with /

#STATIC_ROOT = ROOT_DIR + '/web/static/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static/media'))
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lf5^105_(pe3#4v^^&mp)mq197elaz$#^8d#f*$*zvu@1_j9dg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
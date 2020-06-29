from .base import *

ALLOWED_HOSTS = ['52.78.8.100', 'django.pybo.kr']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '=eKmx$&ymn$wNC|rNT$SX55*RdjKK1G&',
        'HOST': 'ls-be78fd2c2e6b5261442d7480def69d46b156e2c9.cqlcyugj7ibs.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

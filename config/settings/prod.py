from .base import *

ALLOWED_HOSTS = ['52.78.8.100', 'pybo.kr']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'pybo',
#         'USER': 'pybo',
#         'PASSWORD': 'v[E}0dWWYj*EDh+5ivKe~Zult0mG&E8&',
#         'HOST': 'ls-e4fc508cb81e4d605579d0d07ce9344d54cb552d.cqlcyugj7ibs.ap-northeast-2.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }

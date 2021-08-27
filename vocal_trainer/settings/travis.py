from . import *


DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': '',
       'PORT': '',
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
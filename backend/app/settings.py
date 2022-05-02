from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
    'album',
    'authentication',
]

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
     ]
}

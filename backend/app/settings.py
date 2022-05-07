from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
    'album',
    'authentication',
    'django_filters',
]

REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'garpix_auth.rest.authentication.MainAuthentication',
    'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    'rest_framework_social_oauth2.authentication.SocialAuthentication'),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'}





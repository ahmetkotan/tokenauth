from django.conf import settings

class APISettings(object):
    TOKEN_EXPIRATION_TIME = getattr(settings, 'TOKEN_EXPIRATION_TIME', 60 * 60 * 24 * 3) # 3 days
    TOKEN_PREFIX = getattr(settings, 'TOKEN_PREFIX', 'Bearer')
    TOKEN_REFRESH = getattr(settings, 'TOKEN_REFRESH', True)

api_settings = APISettings()
from rest_framework import exceptions

from tokenauth.models import SimpleToken
from tokenauth.api_settings import api_settings

import datetime


class TokenAuthentication(object):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', b'').split()

        if not auth or auth[0] != api_settings.TOKEN_PREFIX:
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed("Invalid token header. No credentials provided.")
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed("Invalid token header. Token string should not contain spaces.")

        try:
            token_key = auth[1]
        except UnicodeError:
            raise exceptions.AuthenticationFailed("Invalid token header. Token string should not contain invalid characters.")

        try:
            token = SimpleToken.objects.get(key=token_key)
        except SimpleToken.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token.")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted.")

        delta = datetime.datetime.now() - token.timestamp.replace(tzinfo=None)
        if delta.seconds > api_settings.TOKEN_EXPIRATION_TIME:
            raise exceptions.AuthenticationFailed("Token expired.")

        return (token.user, token)

    def authenticate_header(self, request):
        return api_settings.TOKEN_PREFIX
from django.shortcuts import render
from django.contrib.auth import authenticate, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.status import HTTP_204_NO_CONTENT

from tokenauth.serializers import TokenLoginSerializer, TokenRefreshSerializer
from tokenauth.models import SimpleToken
from tokenauth.api_settings import api_settings

# Create your views here.

class SimpleTokenLoginView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = TokenLoginSerializer
    refresh_serializer_class = TokenRefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if user:
            token, created = SimpleToken.objects.get_or_create(user=user)
            if not created:
                token.delete()
                token = SimpleToken.objects.create(user=user)

            return Response({'token': token.key})
        else:
            raise AuthenticationFailed('Invalid username/password')

    def put(self, request):
        if not api_settings.TOKEN_REFRESH:
            raise AuthenticationFailed('Token refreshing disallowed')

        serializer = self.refresh_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        key = serializer.validated_data.get('key', None)
        if key:
            try:
                token = SimpleToken.objects.get(key=key)
                user = token.user
                token.delete()
                new_token = SimpleToken.objects.create(user=user)

                return Response({'token': new_token.key})
            except SimpleToken.DoesNotExist:
                raise AuthenticationFailed('Invalid token')
        else:
            raise AuthenticationFailed('Invalid token')


    def delete(self, request):
        if request.user.is_authenticated():
            token, created = SimpleToken.objects.get_or_create(user=request.user)
            logout(request)
            token.delete()

        return Response(status=HTTP_204_NO_CONTENT)

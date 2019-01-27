from rest_framework import serializers
from django.contrib.auth import get_user_model

from tokenauth.validators import token_validator

class TokenLoginSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(TokenLoginSerializer, self).__init__(*args, **kwargs)
        self.fields[get_user_model().USERNAME_FIELD] = serializers.CharField()

    password = serializers.CharField(
        style={'input_type': 'password'},
        label="Password"
    )

class TokenRefreshSerializer(serializers.Serializer):
    key = serializers.CharField(
        label="Token Key",
        required=True,
        validators=[token_validator]
    )

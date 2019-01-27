from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
import hashlib
import binascii
import uuid
import random


class SimpleToken(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name='token_user'
    )

    key = models.CharField(
        max_length=64,
        null=True, blank=True
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def save(self, *args, **kwargs):
        salt = settings.SECRET_KEY.encode('utf-8')
        iteration = random.randint(100000, 200000)
        token = uuid.uuid4().bytes
        derivation = hashlib.pbkdf2_hmac('sha256', token, salt, iteration)

        self.key = binascii.hexlify(derivation)

        super(SimpleToken, self).save(*args, **kwargs)

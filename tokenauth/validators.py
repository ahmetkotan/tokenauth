from django.core.exceptions import ValidationError

import re

def token_validator(value):
    token_patt = re.compile("[a-f0-9]{64}")

    if token_patt.match(value):
        return value
    else:
        raise ValidationError("Invalid Token.")



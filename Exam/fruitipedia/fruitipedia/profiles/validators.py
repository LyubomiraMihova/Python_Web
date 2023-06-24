from django.core.exceptions import ValidationError


def validate_name(value):
    first_char = value[0]
    if not first_char.lower().isalpha():
        raise ValidationError('Your name must start with a letter!')

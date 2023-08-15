from django.core.exceptions import ValidationError


def validate_age(value):
    if value < 18:
        raise


def validate_year(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')

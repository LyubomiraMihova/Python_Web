from enum import Enum

from django.core import validators
from django.db import models

from car_collection_app.web.validators import validate_year


def validate_age(value):
    if value < 18:
        raise


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2

    MIN_VALUE_AGE = 18

    MAX_LEN_PASSWORD = 30

    MAX_LEN_NAME = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME, message='The username must be a minimum of 2 chars'),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_AGE),
        )
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class CarTypes(ChoicesEnum):
    SPORTS = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'


class Car(models.Model):
    MAX_LEN_TYPE = 10

    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2

    MIN_VALUE_PRICE = 1

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=CarTypes.choices(),
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MODEL),
        )
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(validate_year,),
    )

    image_URL = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        )
    )

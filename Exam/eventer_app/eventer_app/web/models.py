from django.core import validators
from django.db import models

from eventer_app.web.mixins import ChoicesLengthMixin, ChoicesMixin
from eventer_app.web.validators import \
    validate_password_at_least_one_digit, validate_date_not_in_past, validate_name_only_letters


class ProfileModel(models.Model):
    MAX_LENGTH_FIRST_NAME = 20

    MIN_LENGTH_LAST_NAME = 4
    MAX_LENGTH_LAST_NAME = 30

    MAX_LENGTH_EMAIL = 45

    MIN_LENGTH_PASSWORD = 5
    MAX_LENGTH_PASSWORD = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=False,
        blank=False,
        validators=(
            validate_name_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
        )
    )

    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_PASSWORD),
            validate_password_at_least_one_digit,
        )
    )


class Categories(ChoicesLengthMixin, ChoicesMixin):
    SPORTS = 'Sports'
    FESTIVALS = 'Festivals'
    CONFERENCES = 'Conferences'
    PERFORMING_ART = 'Performing Art'
    CONCERTS = 'Concerts'
    THEME_PARTY = 'Theme Party'
    OTHER = 'Other'


class EventModel(models.Model):
    MIN_LENGTH_EVENT_NAME = 2
    MAX_LENGTH_EVENT_NAME = 30

    MAX_LENGTH_CATEGORY = 100

    event_name = models.CharField(
        max_length=MAX_LENGTH_EVENT_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_EVENT_NAME),
        ),
        verbose_name='Name',
    )

    category = models.CharField(
        max_length=Categories.max_length(),
        null=False,
        blank=False,
        choices=Categories.choices(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date = models.DateField(
        null=False,
        blank=False,
        validators=(
            validate_date_not_in_past,
        )
    )

    event_image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Event Image',
    )

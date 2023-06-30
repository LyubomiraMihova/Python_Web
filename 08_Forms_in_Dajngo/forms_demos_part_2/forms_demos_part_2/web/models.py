from django.db import models

from forms_demos_part_2.web.validators import ValueInRangeValidator, validate_text


class Todo(models.Model):
    MAX_LEN_TEXT = 25
    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )


class Person(models.Model):
    MAX_LEN_NAME = 20
    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    profile_image = models.ImageField(
        upload_to='people',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

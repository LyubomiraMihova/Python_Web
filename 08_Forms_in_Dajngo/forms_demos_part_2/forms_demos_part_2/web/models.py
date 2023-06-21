from django.db import models

from forms_demos_part_2.web.validators import ValueInRangeValidator, validate_text


# Create your models here.

class ToDo(models.Model):
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
            ValueInRangeValidator(1, 10)
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

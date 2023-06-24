from django.db import models

from fruitipedia.profiles.validators import validate_name


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        # min_length=2,
        validators=(
            validate_name,
        ),
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=35,
        # min_length=1,
        validators=(
            validate_name,
        ),
    )

    email = models.EmailField(
        blank=True,
        null=True,
        max_length=40,
    )

    password = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        # min_length=8,
        # password field- widget in forms
    )

    image = models.URLField()

    age = models.PositiveIntegerField(
        default=18,
    )

from django.db import models


# Create your models here.

class Fruit(models.Model):
    name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        # min_length=2,
        # The name only letters.Otherwise raise ValidationError with the following message: "Fruit name should contain only letters!"
    )

    image = models.URLField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
#
# The fields Name and Pet Photo are required:
# • Name - it should consist of a maximum of 30 characters.
# • Personal Pet Photo - the user can link a picture using a URL
# The field date of birth is optional:
# • Date of Birth - pet's day, month, and year of birth
# Slug - a slug automatically generated using the pet's name and the pet's id, separated by a "-" (dash)

class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_pet_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}--{self.pk}')
        return super().save(*args, **kwargs)

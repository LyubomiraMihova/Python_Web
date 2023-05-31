from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    level = models.CharField(
        max_length=25,
        choices=(
            ('jr', 'Junior'),
            ('reg', 'Regular'),
            ('sr', 'Senior'),
        )
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}, Name: {self.fullname}'


class Department(models.Model):
    name = models.CharField(max_length=15)

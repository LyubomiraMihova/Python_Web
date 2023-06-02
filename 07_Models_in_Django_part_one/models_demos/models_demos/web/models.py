from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(unique=True)
    works_full_time = models.BooleanField()
    job_level = models.CharField(
        max_length=20,
        default='Junior'
    )
    photo = models.URLField()
    birth_date = models.DateField()

    created_on = models.DateTimeField(
        auto_now_add=True
    )


    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'
# class Manager(models.Model):
#     pass

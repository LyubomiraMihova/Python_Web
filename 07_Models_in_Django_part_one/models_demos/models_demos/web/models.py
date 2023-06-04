from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    slug = models.SlugField(
        unique=True,
    )


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    works_full_time = models.BooleanField()
    # job_level = models.CharField(
    #     choices=(
    #         ('jr', 'Junior'),
    #         ('reg', 'Regular'),
    #         ('sr', 'Senior'),
    #     )
    # )
    photo = models.URLField()
    birth_date = models.DateField()

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    # department = models.ForeignKey(
    #     Department,
    #     on_delete=models.CASCADE
    # )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'

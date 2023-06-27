from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'{self.pk} {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True
    )
    deadline = models.DateField()


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(max_length=20)
    years_of_experience = models.PositiveIntegerField()
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

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    projects = models.ManyToManyField(Project)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

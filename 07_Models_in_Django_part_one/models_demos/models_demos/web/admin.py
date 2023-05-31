from django.contrib import admin

# Register your models here.

from models_demos.web.models import Employee
from models_demos.web.models import Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


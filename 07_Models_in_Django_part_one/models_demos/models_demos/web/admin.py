from django.contrib import admin

from models_demos.web.models import Employee, Department, NullBlankDemo, Project


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('email_address',)
    search_fields = ('first_name', 'last_name')
    fieldsets = [
        ('Personal Info', {
            'fields': ('first_name', 'last_name')
        }
         ),
        (
            'Professional Info', {
                'fields': ('email_address', 'birth_date')
            }
        )
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass

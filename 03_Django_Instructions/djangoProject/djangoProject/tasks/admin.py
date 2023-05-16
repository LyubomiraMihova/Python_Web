from django.contrib import admin
from djangoProject.tasks.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'priority')


admin.site.register(Task, TaskAdmin)

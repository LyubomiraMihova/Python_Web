from django.contrib import admin

from eventer_app.web.models import ProfileModel, EventModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    pass

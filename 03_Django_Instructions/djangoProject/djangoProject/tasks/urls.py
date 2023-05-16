# urls for tasks app
from django.urls import path
from djangoProject.tasks.views import index

urlpatterns = [
    path('', index)
]

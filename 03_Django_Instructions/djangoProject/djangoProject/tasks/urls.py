# urls for tasks app
from django.urls import path
from djangoProject.tasks.views import index, list_tasks_template
# , list_tasks

urlpatterns = [
    path('', index),
    # path('list/', list_tasks)
    path('with-template/', list_tasks_template)
]

# urls for tasks app
from django.urls import path
from djangoProject.tasks.views import index, list_tasks_template, show_all_tasks

# , list_tasks

urlpatterns = (
    path('', index),
    # path('list/', list_tasks)
    path('with-template/', list_tasks_template),
    path('all/', show_all_tasks)
)

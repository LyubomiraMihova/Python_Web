from django.urls import path

from django101.tasks.views import show_bare_minimum_view, show_all_tasks, index

urlpatterns = [
    path('', index),
    path('it-works/', show_bare_minimum_view, name='it is working'),
    path('all/', show_all_tasks, name='all tasks'),
]

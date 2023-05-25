from django.urls import path

from django101.exercising.views import index, this_is_function, view_one, view_two

urlpatterns = [
    path('', index),
    path('function/', this_is_function),
    path('page/', view_one, name='webpage1'),
    path('page/<int:id>', view_two, name='webpage2'),
]

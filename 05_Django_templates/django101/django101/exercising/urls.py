from django.urls import path

from django101.exercising.views import index, this_is_function

urlpatterns = [
    path('', index),
    path('function/', this_is_function)
]
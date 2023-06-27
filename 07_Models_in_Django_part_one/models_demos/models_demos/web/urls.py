from django.urls import path

from models_demos.web.views import index, next_index

urlpatterns = [
    path('', index, name='index'),
    # path('delete/<int:pk>/', delete_employee, name='delete employee'),
    path('next-index', next_index, name='next index'),
]

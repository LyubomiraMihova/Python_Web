from django.urls import path

from models_demos.web.views import index

urlpatterns = [
    path('', index, name='index'),
    # path('delete/<int:pk>/', delete_employee, name='delete employee'),
]

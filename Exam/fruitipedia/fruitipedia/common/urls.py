from django.urls import path

from fruitipedia.common.views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]

from django.urls import path, include
from .views import photo_details, photo_edit, PhotoAddView

urlpatterns = [
    path('add/', PhotoAddView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', photo_details, name='photo details'),
        path('edit/', photo_edit, name='photo edit'),
    ])),
]

from django.urls import path, include

from petstagram_project.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = [
    path('add/', add_pet, name='pet add'),
    path('add/<str:username>/pet/<slug:pet_name>', include([
        path('', details_pet, name='pet details'),
        path('edit/', edit_pet, name='pet edit'),
        path('delete/', delete_pet, name='pet delete'),
    ]))
]

from django.urls import path

from forms_demos_part_2.web.views import index, create_person, list_people

urlpatterns = [
    path('', index, name='index'),
    path('people/', list_people, name='list people'),
    path('people/create/', create_person, name='create person'),
]

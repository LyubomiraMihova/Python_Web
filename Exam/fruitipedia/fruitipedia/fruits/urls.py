from django.urls import path, include

from fruitipedia.fruits.views import create_fruit, details_fruit, edit_fruit, delete_fruit

urlpatterns = [
    path('create/', create_fruit, name='create fruit'),
    path('<int:fruit_id>/', include([
        path('details/', details_fruit, name='details fruit'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit'),
    ])),
]

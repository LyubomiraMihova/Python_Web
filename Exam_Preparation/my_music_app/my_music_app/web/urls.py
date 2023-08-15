from django.urls import path, include

from my_music_app.web.views import index, \
    add_album, details_album, edit_album, delete_album, \
    details_profile, delete_profile

'''
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add albums page
•	http://localhost:8000/album/details/<id>/ - albums details page
•	http://localhost:8000/album/edit/<id>/ - edit albums page
•	http://localhost:8000/album/delete/<id>/ - delete albums page
•	http://localhost:8000/profile/details/ - profiles details page
•	http://localhost:8000/profile/delete/ - delete profiles page
'''

urlpatterns = [
    path('', index, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add albums page'),
        path('details/<int:pk>/', details_album, name='albums details page'),
        path('edit/<int:pk>/', edit_album, name='edit albums page'),
        path('delete/<int:pk>/', delete_album, name='delete albums page'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='profiles details page'),
        path('delete/', delete_profile, name='delete profiles page'),
    ])),
]

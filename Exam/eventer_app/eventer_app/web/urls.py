from django.urls import path, include

from eventer_app.web.views import index, \
    create_event, details_event, edit_event, delete_event, \
    create_profile, details_profile, edit_profile, delete_profile, dashboard

urlpatterns = [
    path('', index, name='home page'),
    path('dashboard/', dashboard, name='dashboard page'),
    path('create/', create_event, name='create event page'),
    path('details/<int:pk>/', details_event, name='event details page'),
    path('edit/<int:pk>/', edit_event, name='edit event page'),
    path('delete/<int:pk>/', delete_event, name='delete event page'),
    path('profile/', include([
        path('create/', create_profile, name='create profile page'),
        path('details/', details_profile, name='profile details page'),
        path('edit/', edit_profile, name='edit profile page'),
        path('delete/', delete_profile, name='delete profile page'),
    ])),
]

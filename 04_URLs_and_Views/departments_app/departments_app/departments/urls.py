from django.urls import path
from departments_app.departments.views import sample_view, show_departments, redirect_to_first_department, \
    show_not_found

urlpatterns = (
    path('', sample_view),
    path('<int:department_id>/', sample_view),
    path('dep', show_departments, name='show departments'),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('not-found/', show_not_found, name='not found'),
)
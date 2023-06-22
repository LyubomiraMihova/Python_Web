from django.urls import path

from departments_app.departments.views import sample_view, show_department_details, redirect_to_first_department

urlpatterns = [
    # path('', sample_view),
    path('<int:department_id>/', show_department_details, name='show departments'),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
]

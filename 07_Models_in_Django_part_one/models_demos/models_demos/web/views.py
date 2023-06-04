from django.shortcuts import render, redirect
from models_demos.web.models import Employee, Department


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(id=1)
    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'web/index.html', context)


# def delete_employee(request, pk):
#     employee = employees(Employee, pk=pk)
#     employee.delete()
#     return redirect('index')

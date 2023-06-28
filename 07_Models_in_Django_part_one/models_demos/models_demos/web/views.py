from django.shortcuts import render, redirect, get_object_or_404
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


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def next_index(request):
    employees = Employee.objects.filter(department_id=1) \
        .order_by('last_name', 'first_name')
    print(employees)
    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'department': department,
    }

    return render(request, 'web/next-index.html', context)

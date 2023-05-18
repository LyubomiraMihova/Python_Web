from django.shortcuts import render
from django.http import HttpResponse
from djangoProject.tasks.models import Task

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def list_tasks(request):
#     all_tasks = Task.objects.all()
#
#     return HttpResponse(f'{t.id} {t.title} {t.priority}' for t in all_tasks)

def list_tasks_template(request):
    return render(request, 'tasks.html')

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    return (all_tasks)

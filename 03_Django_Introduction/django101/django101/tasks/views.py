from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


# Create your views here.

def show_bare_minimum_view(request):
    return HttpResponse('It works')


def show_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.name} {t.id}' for t in all_tasks)
    return HttpResponse(result)


def index(request):
    all_tasks = Task.objects.all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)

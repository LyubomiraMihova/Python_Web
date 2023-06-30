from django.http import HttpResponse
from django.shortcuts import render

from forms_demos_part_2.web.forms import TodoCreateForm, PersonCreateForm
from forms_demos_part_2.web.models import Person


def index(request):
    if request.method == 'GET':
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def list_people(request):
    context = {
        'people': Person.objects.all()
    }
    return render(request, 'list-people.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'create-person.html' , context)

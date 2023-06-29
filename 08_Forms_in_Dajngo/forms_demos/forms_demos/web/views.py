from django import forms
from django.shortcuts import render

from forms_demos.web.forms import PersonForm, PersonCreateForm
from forms_demos.web.models import Person


# from forms_demos.web.models import Person
# from forms_demos.web.forms import PersonForm


# Create your views here.


def index_form(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


def index_model_forms(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }

    return render(request, 'model_forms.html', context)

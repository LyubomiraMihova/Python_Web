from django import forms
from django.shortcuts import render


# from forms_demos.web.forms import NameForm

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


# Create your views here.


def index(request):
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'web/index.html', context)

from django.shortcuts import render

# Create your views here.

from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


def index(request):
    if request.method == 'POST':
        print(request.POST)
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
    else:
        form = NameForm()
        name = None

    context = {
        'form': form
    }
    return render(request, 'web/index.html', context)

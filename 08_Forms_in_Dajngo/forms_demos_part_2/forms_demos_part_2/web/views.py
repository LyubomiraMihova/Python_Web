from django.http import HttpResponse
from django.shortcuts import render

from forms_demos_part_2.web.forms import ToDo


# Create your views here.


def index(request):
    if request.method == 'GET':
        form = ToDo()
    else:

        form = ToDo(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

from random import choice

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound


# Create your views here.

def sample_view(request, *args, **kwargs):
    body = f'path: {request.path}, args={args}, kwargs={kwargs}'
    return HttpResponse(body)


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }

    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # return redirect(f'/departments/?order_by={order_by}')
    return redirect('show departments')


def show_not_found(request):
    return HttpResponseNotFound()


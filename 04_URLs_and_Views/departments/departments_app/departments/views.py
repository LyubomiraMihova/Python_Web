from random import choice

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.

def sample_view(request, *args, **kwargs):
    pass


def show_department_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    return redirect('show departments', department_id=13)


def show_not_found(request):
    status_code = 400
    # return HttpResponseNotFound('This is not found!')
    return HttpResponse('Error', status=status_code)
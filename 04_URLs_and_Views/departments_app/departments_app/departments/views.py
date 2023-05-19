from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample_view(request, *args, **kwargs):
    body = f'path: {request.path}, args={args}, kwargs={kwargs}'
    return HttpResponse(body)

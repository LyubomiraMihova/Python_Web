from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'first_name': 'John',
        'last_name': 'Smith',
        'department': 'Marketing',
        'email_address': 'john.smith@company.com',
        'info': {'name': 'Lyubomira Velinova', 'age': 30},
        'person': Person('Lyubomira', 30),
        'people': ['Maria', 'Mark', 'Gena', 'Travis'],
        'sum': 26.77633892,
    }

    return render(request, 'index.html', context)


def this_is_function(request):
    return HttpResponse('This is just function')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'This is {self.name} and she/he is {self.age} years old.'

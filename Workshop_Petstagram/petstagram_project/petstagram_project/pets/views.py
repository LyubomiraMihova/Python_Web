from django.shortcuts import render


# Create your views here.

def add_pet(request):
    render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, pet_name):
    render(request, 'pets/pet-delete-page.html')


def edit_pet(request, username, pet_name):
    render(request, 'pets/pet-edit-page.html')


def details_pet(request, username, pet_name):
    render(request, 'pets/pet-details-page.html')

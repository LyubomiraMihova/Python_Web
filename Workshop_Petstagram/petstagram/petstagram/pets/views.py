from django.shortcuts import render


# Create your views here.

def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, pet_name):
    return render(request, 'pets/pet-details-page.html')


def pet_edit(request, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, pet_name):
    return render(request, 'pets/pet-delete-page.html')

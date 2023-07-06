from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Pet


# Create your views here.

@login_required
def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


@login_required
def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pets/pet-details-page.html', context)


@login_required
def pet_edit(request, pet_name):
    return render(request, 'pets/pet-edit-page.html')


@login_required
def pet_delete(request, pet_name):
    return render(request, 'pets/pet-delete-page.html')

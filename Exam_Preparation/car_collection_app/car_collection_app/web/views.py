from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def catalogue(request):
    return render(request, 'core/catalogue.html')


def car_create(request):
    return render(request, 'car/car-create.html')


def car_details(request, pk):
    return render(request, 'car/car-details.html')


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request, pk):
    return render(request, 'car/car-delete.html')


def profile_create(request):
    return render(request, 'profile/profile-create.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')

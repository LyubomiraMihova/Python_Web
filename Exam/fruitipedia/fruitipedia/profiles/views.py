from django.shortcuts import render

from fruitipedia.profiles.forms import ProfileForm


# Create your views here.

def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/dashboard.html')

    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    return render(request, 'profiles/details-profile.html')


def edit_profile(request):
    return render(request, 'profiles/edit-profile.html')


def delete_profile(request):
    return render(request, 'profiles/delete-profile.html')

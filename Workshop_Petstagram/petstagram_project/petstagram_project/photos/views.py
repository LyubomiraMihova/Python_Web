from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from petstagram_project.photos.models import Photo


# Create your views here.

@login_required
def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {
        'photo': photo,
        'likes': photo.like_set.count(),
        'comments': photo.comment_set.all(),
    }
    return render(request, 'photos/photo-details-page.html', context)


@login_required
def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')

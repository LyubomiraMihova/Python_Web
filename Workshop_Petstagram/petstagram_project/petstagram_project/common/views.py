from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_project.common.models import Like
from petstagram_project.photos.models import Photo


# Create your views here.

def index(request):
    context = {
        'all_photos': Photo.objects.all()
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo__id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        new_like_object = Like(to_photo=photo)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

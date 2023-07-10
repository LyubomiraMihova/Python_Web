from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_project.common.forms import SearchForm, CommentForm
from petstagram_project.common.models import Like
from petstagram_project.photos.models import Photo


# Create your views here.

def index(request):
    photos = Photo.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        photos = photos.filter(tagged_pets__name__icontains=search_text)

    for photo in photos:
        photo.liked_by_user = photo.like_set \
            .filter(user=request.user) \
            .exists()

    context = {
        'all_photos': photos,
        'comment_form': CommentForm(),
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)

    kwargs = {
        'to_photo': photo,
        'user': request.user,
    }

    liked_object = Like.objects \
        .filter(**kwargs) \
        .first()

    if liked_object:
        liked_object.delete()
    else:
        new_like_object = Like(**kwargs)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

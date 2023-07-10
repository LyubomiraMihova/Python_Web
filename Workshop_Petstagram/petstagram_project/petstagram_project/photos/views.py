from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram_project.photos.forms import PhotoAddForm
from petstagram_project.photos.models import Photo


class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoAddForm

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


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

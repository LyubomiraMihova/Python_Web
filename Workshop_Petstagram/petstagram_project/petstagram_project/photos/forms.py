from django import forms

from petstagram_project.photos.models import Photo


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [ 'description', 'location', 'tagged_pets', 'user']

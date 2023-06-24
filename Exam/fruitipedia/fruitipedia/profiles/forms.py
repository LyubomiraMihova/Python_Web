from django import forms
from django.forms import CharField

from fruitipedia.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # widgets = {
        #     'first_name': CharField(
        #         attrs={
        #             'placeholder': 'First Name'
        #         }
        #     )
        # }

        fields = ('first_name', 'last_name', 'email', 'password')

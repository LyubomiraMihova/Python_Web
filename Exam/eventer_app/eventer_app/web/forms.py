from django import forms

from eventer_app.web.models import ProfileModel, EventModel


class ProfileBaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'profile_picture', 'password']


class EditProfileForm(ProfileBaseForm):
    pass


class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            EventModel.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'


class CreateEventForm(EventBaseForm):
    pass


class DeleteEventForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True

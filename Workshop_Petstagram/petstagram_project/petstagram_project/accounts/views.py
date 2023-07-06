from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


# def register_user(request):
#     return render(request, 'accounts/register-page.html')


def edit_user(request):
    return render(request, 'accounts/profile-edit-page.html')


def details_user(request):
    return render(request, 'accounts/profile-details-page.html')


def delete_user(request):
    return render(request, 'accounts/profile-delete-page.html')

# def login_user(request):
#     return render(request, 'accounts/login-page.html')

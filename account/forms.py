from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')




class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email')

    error_messages = {
        'invalid_login': "Please enter a correct email and password. Note that both fields may be case-sensitive.",

    }

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django import forms


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'input-field', 'placeholder': 'username'}))
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'input-field', 'placeholder': 'password'}))

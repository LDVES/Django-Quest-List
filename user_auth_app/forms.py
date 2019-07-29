from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder' : 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder' : 'Password'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs=
    {
    'class': "form-control",
    'placeholder' : 'Email'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs=
    {
    'class': "form-control",
     'placeholder' : 'Username'
     }))

    password1 = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs=
    {
    'class': "form-control",
    'placeholder' : 'Password'
    }))

    password2 = forms.CharField(label = "Confirm password", widget=forms.PasswordInput(attrs=
    {
    'class': "form-control",
     'placeholder' : 'Confirm Password'
    }))

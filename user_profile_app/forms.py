from django import forms

class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs=
    {
        'class': "form-control",
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(label="New password", widget=forms.PasswordInput(attrs=
    {
        'class': "form-control",
        'placeholder': 'Confirm Password'
    }))
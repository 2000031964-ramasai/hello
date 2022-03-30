
from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ['username', 'password', 'confirmation', 'phoneno', 'email', 'address']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Register
        fields = ['username', 'password']

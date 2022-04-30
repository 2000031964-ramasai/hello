from django import forms
from .models import Register
from .models import Profile
from .models import Contact
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'gender', 'acres', 'kharif', 'rabi', 'loan']
        models = {'name': 'Name', 'age': 'Age', 'gender': 'Gender', 'kharif': 'Kharif', 'rabi': 'Rabi', 'loan': 'Loan'}


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = ['name', 'email','phone','message']
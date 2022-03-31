from django import forms
from .models import Register
from .models import Profile


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'gender', 'acres', 'kharif', 'rabi', 'loan']
        models = {'name': 'Name', 'age': 'Age', 'gender': 'Gender', 'kharif': 'Kharif', 'rabi': 'Rabi', 'loan': 'Loan'}

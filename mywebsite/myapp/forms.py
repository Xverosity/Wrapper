# myapp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReportForm(forms.Form):
    file = forms.FileField(label='Upload Photo/Video', widget=forms.FileInput)
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'rows': 4}))

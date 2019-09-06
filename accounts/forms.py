from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class RegisterForm(UserCreationForm):
    icon = forms.ImageField(required=False, error_messages = {'invalid':"Images only"}, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "icon", "password1", "password2"]

class EditProfileForm(UserChangeForm):
    icon = forms.ImageField(required=False, error_messages = {'invalid':"Images only"}, widget=forms.FileInput)
    username = forms.CharField(required=False)
    password = None
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "icon"]
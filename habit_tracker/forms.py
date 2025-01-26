from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Habit


class Habitform(ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'completed']
        labels = {
            'title': '',
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
            
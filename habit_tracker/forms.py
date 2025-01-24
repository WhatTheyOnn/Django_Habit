from django import forms
from django.forms import ModelForm

from .models import *


class Habitform(ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'
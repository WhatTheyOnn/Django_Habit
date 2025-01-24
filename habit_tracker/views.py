from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def index(request):
    habit = Habit.objects.all()

    form = Habitform()

    context = {'habits': habit, 'form': form}
    return render(request, 'Habit_tracker/list.html', context)
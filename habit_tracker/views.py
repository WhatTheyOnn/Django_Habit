from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def index(request):
    habit = Habit.objects.all()

    form = Habitform()

    if request.method == 'POST':
        form = Habitform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'habits': habit, 'form': form}
    return render(request, 'Habit_tracker/list.html', context)
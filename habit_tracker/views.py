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

def updateHabit(request, pk):
    habit = Habit.objects.get(id=pk)

    form = Habitform(instance=habit)

    if request.method == 'POST':
        form = Habitform(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Habit_tracker/Habit_update.html', context)
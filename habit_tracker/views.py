from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm



def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'Habit_tracker/Accounts/register.html', context)

def loginPage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'Habit_tracker/Accounts/login.html')
    context = {}
    return render(request, 'Habit_tracker/Accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



def index(request):
    habit = Habit.objects.all()
    form = Habitform()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Habitform(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')
        else:
            return redirect('login')

    context = {'habits': habit, 'form': form}
    return render(request, 'Habit_tracker/list.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteHabit(request, pk):
    item = Habit.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'Habit_tracker/delete.html', context)
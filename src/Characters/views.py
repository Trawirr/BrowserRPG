from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Characters.models import *
from RanksClasses.models import *

def hello(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'character.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_character = Character(user=user, rank=Rank.objects.get(value=1))
            new_character.save()
            login(request, user)
            return redirect('character')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
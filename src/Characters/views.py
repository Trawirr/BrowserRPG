from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Characters.models import *
from RanksClasses.models import *
from Characters.utils.utils import *
from Enemies.utils.utils import *
import numpy as np

def hello(request):
    context = {}
    if request.user.is_authenticated:
        context['character'] = request.user.characters
    return render(request, 'index.html', context)

def profile(request):
    if request.user.is_authenticated:
        context = {}    
        return render(request, 'character.html', context)
    else: return redirect('login')

def memories(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            memory_id = int(request.POST['memory_id'])
            memory = Memory.objects.get(id=memory_id)
            character = request.user.characters
            equip(character, memory)
        context = {}
        return render(request, 'memories.html', context)
    else: return redirect('login')

def training(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            shards = int(request.POST['shards'])
            character = request.user.characters
            if character.shards >= shards:
                character.shards -= shards
                character.soul_core += shards
                character.save()
            else:
                messages.error(request, 'Incorrect number of shards')
        context = {}
        return render(request, 'training.html', context)
    else: return redirect('login')

def hunt(request):
    if request.user.is_authenticated:
        character = request.user.characters
        enemy = get_random_enemy(character.region)
        logs = battle(character, enemy)
        context = {"enemy": enemy, "logs": logs}
        return render(request, 'hunt.html', context)
    else: return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            new_character = Character(user=user, rank=Rank.objects.get(value=1))
            new_character.save()
            
            probs = [1/2**i for i in range(1,8)]
            probs_np = np.array(probs) / sum(probs)
            new_aspect = create_aspect(np.random.choice(range(1,8), 1, p=probs_np), new_character)
            new_aspect.save()

            for i in range(2):
                new_ability = create_ability(new_aspect.attributes, new_character)
                new_ability.save()

            new_flaw = create_flaw(new_aspect.rank.value, new_character)
            new_flaw.save()

            login(request, user)
            return redirect('profile')
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
            return redirect('profile') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Item

def home(request):
    
    queryResult = Item.objects.all();

    return render(request, 'home.html', {'queryResult':queryResult})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você entrou em sua conta com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro ao entar, tente novamente...")

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home') 
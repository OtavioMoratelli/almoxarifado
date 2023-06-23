from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Item, HistoricoEmprestimo

def home(request):
    return render(request, 'home.html', {})

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

def itens_emp(request):
    if not request.user.is_authenticated:
        messages.error(request, "Erro, você não está cadastrado")
        return redirect('login')
    
    queryResult = Item.objects.all();

    return render(request, 'itens.html', {'queryResult':queryResult})

def emprestimos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Erro, você não está cadastrado")
        return redirect('login')
    
    queryEmprestimo = HistoricoEmprestimo.objects.filter(id_consumidor = request.user.consumidor.id_pessoa);

    return render(request, 'emprestimos.html', {'queryEmprestimo' : queryEmprestimo})

def novoEmprestimo(request):


    return render(request, 'novo_emprestimo.html', {})
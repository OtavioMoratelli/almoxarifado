from django.shortcuts import render, redirect
from .models import Item

def home(request):
    
    queryResult = Item.objects.all();

    return render(request, 'home.html', {'queryResult':queryResult})



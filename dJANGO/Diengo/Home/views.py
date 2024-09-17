from django.shortcuts import render
from Diengo import urls

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
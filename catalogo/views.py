from django.shortcuts import render
from .models import Index, Info, Formulario, Galeria, We
from django.views import generic

# Create your views here.
def index(request):
    return render(request, '../templates/index.html', {})

def info(request):
    return render(request, '../templates/info.html', {})

def formulario(request):
    return render(request, '../templates/formulario.html', {})

def galeria(request):
    return render(request, '../templates/galeria.html', {})

def we(request):
    return render(request, '../templates/we.html', {})
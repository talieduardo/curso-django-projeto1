from django.http import HttpResponse
from django.shortcuts import render  # PARA IMPORTAR A PÁGINA HTML


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse("Contato2")


def sobre(request):
    return HttpResponse("Sobre2")

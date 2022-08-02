from django.shortcuts import render

# Create your views here.


def index(request):
    return  render(request, 'inicio.html', {'page_title': 'Inicio'})

def contact(request):
    return  render(request, 'contacto.html', {'page_title': 'Contacto'})
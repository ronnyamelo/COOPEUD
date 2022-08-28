from django.shortcuts import render

# Create your views here.


def index(request):
    return  render(request, 'inicio.html', {'title': 'Inicio'})

def contact(request):
    return  render(request, 'contacto.html', {'title': 'Contacto'})

def location(request):
    return  render(request, 'ubicacion.html', {'title': 'Contacto'})

def formulario(request):
    return render(request, 'datosFormulario.html')

def history(request):
    return render(request, 'nosotros.html')
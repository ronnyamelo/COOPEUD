from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'inicio.html') 

def nosotros(request):
    return render(request,'nosotros.html')

def adminViewSet(request):
    return render(request, 'admin/index.html')
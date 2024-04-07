from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from tienda.models import Categoria,Producto


def home(request):
    productos = Producto.objects.all()
    
    return render(request,'proyectowebapp/home.html',{'productos':productos})

def nosotros(request):
    return render(request,'partials/nosotros.html')

def contacto(request):
    return render(request,'partials/contacto.html')


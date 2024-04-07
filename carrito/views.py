from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import Producto


# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("Home")


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("Home")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect("Home")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Home")

from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from tienda.models import Categoria,Producto,Factura
from django.utils import timezone
from datetime import timedelta
from datetime import datetime, timedelta

def home(request):
    productos = Producto.objects.all()
    
    return render(request,'proyectowebapp/home.html',{'productos':productos})

def nosotros(request):
    return render(request,'partials/nosotros.html')

def contacto(request):
    return render(request,'partials/contacto.html')

def registros(request):
    nombre_usuario = request.GET.get('nombre_usuario')
    ultimos_7_dias = request.GET.get('ultimos_7_dias')
    ultimos_15_dias = request.GET.get('ultimos_15_dias')

    fecha_actual = datetime.now().date()
    fecha_inicio_7_dias = fecha_actual - timedelta(days=7)
    fecha_inicio_15_dias = fecha_actual - timedelta(days=15)
    historial = Factura.objects.all()

    if nombre_usuario:
        historial = historial.filter(usuario__username__icontains=nombre_usuario)
    if ultimos_7_dias:
        historial = historial.filter(fecha_compra__gte=fecha_inicio_7_dias, fecha_compra__lte=fecha_actual)

    if ultimos_15_dias:
        historial = historial.filter(fecha_compra__gte=fecha_inicio_15_dias, fecha_compra__lte=fecha_actual)

    return render(request, 'proyectowebapp/historial.html', {'historial': historial})

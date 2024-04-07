from django.contrib import admin
from .models import Categoria,Producto,Factura
from django.db.models import Sum,F
from django.core.exceptions import ValidationError
from django.contrib import messages
from django import forms


@admin.register(Categoria)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'precio','categoria']

    def save_model(self, request, obj, form, change):
        if obj.cantidad < 0:
            messages.error(request, "La cantidad no puede ser un número negativo.")
            return
        elif obj.precio <= 0:
            messages.error(request, "El precio debe ser un número positivo y mayor a cero.")
            return
        else:
            obj.save()

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'producto', 'cantidad','total_a_pagar','fecha_compra']
    list_filter = ['fecha_compra']
    exclude = ['pagado']

    def usuario(self,obj):
        return obj.usuario.first_name if obj.usuario else ''
    

    def save_model(self, request, obj, form, change):
        if obj.cantidad <= 0:
            messages.error(request, "La cantidad no puede ser un número negativo ni igual a cero.")
            return

        if obj.producto.cantidad < obj.cantidad:
            messages.error(request, "No hay suficiente stock")
            return

        if change: 
            old_obj = self.model.objects.get(pk=obj.pk)
            obj.producto.cantidad += old_obj.cantidad  
        obj.producto.cantidad -= obj.cantidad 
        obj.producto.save()
        obj.save()

    def total_a_pagar(self, obj):
        return obj.producto.precio * obj.cantidad
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Factura,Producto

from carrito.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def enviar_mail(request, **kwargs):
    carro = Carro(request)
    productos_factura = []

    for key, value in carro.carro.items():
        factura = Factura.objects.create(
            usuario=request.user,
            producto_id=key,
            cantidad=value["cantidad"]
        )
        productos_factura.append(factura)

    asunto = "Gracias por la compra"
    nombre_usuario = request.user.username

    productos_descripcion = [
        f'{factura.cantidad} unidades de: {factura.producto.nombre}' 
        for factura in productos_factura
    ]

    productos_str = ', '.join(productos_descripcion)

    mensaje = render_to_string("emails/factura.html", {
        "nombre_usuario": nombre_usuario,
        "productos": productos_str
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = "albarracinjuancarlos800@gmail.com"
    to = request.user.email
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
    
    carro.limpiar_carro()

    messages.success(request, "Compra realizada correctamente")
    return redirect("Home")


from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Categoria(models.Model):
    nombre = models.CharField(max_length=150,null=False,blank=False)
    descripcion = models.TextField(null=True,blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120,null=False,blank=False)
    precio = models.IntegerField(null=False,blank=False)
    cantidad = models.IntegerField(null=False,blank=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto", null=False,blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1,null=False,blank=False)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad} unidades de: {self.producto.nombre}'
    
  
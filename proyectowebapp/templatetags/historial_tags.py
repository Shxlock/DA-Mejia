from django import template
from tienda.models import Factura

register = template.Library()

@register.filter
def multiplica(value, arg):
    return value * arg
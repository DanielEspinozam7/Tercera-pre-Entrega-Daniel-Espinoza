from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Cotizacion)
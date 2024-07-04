from django.db import models

# Create your models here.
class Venta(models.Model):
    NroVenta = models.IntegerField()
    Detalle = models.CharField(max_length=50)
    FechaVenta = models.DateField()
    
class Producto(models.Model):
    Titulo = models.CharField(max_length=50)
    Descripicion = models.CharField(max_length=50)
    Especificaciones = models.EmailField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    consultas = models.CharField(max_length=4000)
    
class Cotizacion(models.Model):
    RazonSocial = models.CharField(max_length=50)
    FechaCoti = models.DateField()
    Detalle = models.CharField(max_length=50)







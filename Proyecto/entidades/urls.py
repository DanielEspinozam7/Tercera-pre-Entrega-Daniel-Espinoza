from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('ventas/', ventas, name="ventas"), #Se le dá un nombre para poder cambiar la ruta (ventas/) sin afecar al código
    path('clientes/', clientes, name="clientes"),
    path('productos/', productos, name="productos"),
    path('cotizaciones/', cotizaciones, name="cotizaciones"),
    path('acerca/', acerca, name="acerca"),
    
    #Formularios
        path('clientesForm/', clienteForm, name="clientesForm"),

]

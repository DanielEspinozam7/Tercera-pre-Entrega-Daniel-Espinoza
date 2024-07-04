from django.shortcuts import render
from .models import *
from .form import *

# Create your views here.

def home(request):
    return render(request, "entidades/index.html") #por defecto la app busca en carpeta templates el home.html

def ventas(request):
    #contexto entrega todos los datos o registros que tenga nuestro models
    contexto = {"ventas": Venta.objects.all()}
    return render(request, "entidades/ventas.html", contexto)

def clientes(request):
    contexto = {"clientes": Cliente.objects.all()}
    return render(request, "entidades/clientes.html", contexto)

def productos(request):
    contexto = {"productos": Producto.objects.all()}
    return render(request, "entidades/productos.html", contexto)

def cotizaciones(request):
    contexto = {"cotizaciones": Cotizacion.objects.all()}
    return render(request, "entidades/cotizaciones.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")


#Formulario

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            #creamos las variables que reciben los datos del formulario cliente            
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_correo = miForm.cleaned_data.get("correo")
            consulta_cliente = miForm.cleaned_data.get("consultas")
            
            #Creamos el objeto cliente y les pasamos los datos obtenidos del formulario
            cliente = Cliente(nombre=cliente_nombre, 
                        correo=cliente_correo,
                        consultas=consulta_cliente)
            
            cliente.save()
            contexto = {"clientes": Cliente.objects.all()}
            return render (request, "entidades/clientes.html", contexto)
    else:
        miForm = ClienteForm()
        
    return render (request, "entidades/clientesForm.html", {"form": miForm})


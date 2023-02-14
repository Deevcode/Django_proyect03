from django.shortcuts import render
from .models import Producto

#RUTA DE LA VISTA DE HOME
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'app/home.html', data)

#RUTA DE LA VISTA DE CONTACTO
def contacto(request):
    return render(request, 'app/contacto.html')

#RUTA DE LA VISTA DE GALERIA
def galeria(request):
    return render(request, 'app/galeria.html')
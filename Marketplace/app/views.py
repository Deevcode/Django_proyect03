from django.shortcuts import render
#SE IMPORTA EL MODELO DE PRODUCTO PARA USARLO EN LA RUTA DE HOME
from .models import Producto
#SE IMPORTA EL FORMS DE CONTACTOFORM -> FORMULARIO DE CONTACTO
from .forms import ContactoFrom

#RUTA DE LA VISTA DE HOME
def home(request):
    #INSTANCIA DE LA VARIABLE PRODUCTOS DONDE TRAE TODOS LOS OBJETOS EN EL MODELO DE PRODUCTOS
    productos = Producto.objects.all()
    #ARREGLO DATA DONDE EL STR PASA A SER LA INTANCIA DECLARADA
    data = {
        'productos' : productos
    }
    return render(request, 'app/home.html', data) #DEBES AGREGAR EL ARREGLO EN EL RETORNO

#RUTA DE LA VISTA DE CONTACTO
def contacto(request):
    #ARREGLO DATA STR PASA A SER EL FORMULARIO DE CONTACTO DEL MODELO DECLARADO EN forms.py
    data ={ 
        'form' : ContactoFrom()
    }

    if request.method == 'POST':
        formulario = ContactoFrom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
                
    return render(request, 'app/contacto.html', data) #DEBES AGREGAR EL ARREGLO EN EL RETORNO

#RUTA DE LA VISTA DE GALERIA
def galeria(request):
    return render(request, 'app/galeria.html')
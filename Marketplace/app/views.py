from django.shortcuts import render

#RUTA DE LA VISTA DE HOME
def home(request):
    return render(request, 'app/home.html')

#RUTA DE LA VISTA DE CONTACTO
def contacto(request):
    return render(request, 'app/contacto.html')

#RUTA DE LA VISTA DE GALERIA
def galeria(request):
    return render(request, 'app/galeria.html')
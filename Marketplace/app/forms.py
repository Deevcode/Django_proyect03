#Se importan los formularios de Django
from django import forms
#Se importa el modelo de Contacto desde models
from .models import Contacto

#Se crea el contacto de formulario
class ContactoFrom(forms.ModelForm):

    class Meta:
        model = Contacto
       #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"] #lo puedes hacer campo por campo
        fields = '__all__' #que incluya a todos los campos

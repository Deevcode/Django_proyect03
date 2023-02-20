from django.db import models

#MODELO DE MARCA
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre # retorna el valor mas representativo de la tabla

#MODELO DE PRODUCTO
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT) # (protege los productos asociados a la marca [protect])
    fecha_fabricacion = models.DateField()
    image = models.ImageField(upload_to="productos", null=True)

    def __str__ (self):
        return self.nombre # retorna el valor mas representativo de la tabla

# OPCIONES DE CONSLTA PARA EL TIPO DE CONSULTA
opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

#MODELO DE CONTACTO PARA EL FORMULARIO, SE DEDE IMPORTART EN forms.py DESDE EL DIRECTORIO DE LA APP
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta) # A TRAVEZ DE CHOISES PUEDES PASAR EL ARREGLO DE opciones_consulta
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre # retorna el valor mas representativo de la tabla
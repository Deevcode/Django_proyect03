from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre # retorna el valor mas representativo de la tabla

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

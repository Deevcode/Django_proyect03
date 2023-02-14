from django.contrib import admin
from .models import Marca, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"] #este campo sera editable
    search_fields = ["nombre"] #puede filtar productos por el nombre
    list_filter = ["marca", "nuevo"] #filtros de busqueda
    list_per_page = 5 #lista 

admin.site.register(Marca)
admin.site.register(Producto)
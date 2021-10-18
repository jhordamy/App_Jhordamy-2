from django.contrib import admin
from Jhordamy.models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'direccion', 'celular')
    search_fields = ['nombre']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'direccion', 'celular')
    search_fields = ['cedula']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'categoria', 'descripcion', 'precio')
    search_fields = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ['nombre']

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
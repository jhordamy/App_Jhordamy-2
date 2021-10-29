from django.conf.urls import url
from django.db import models
from django.utils. safestring import mark_safe

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=225, blank=False, unique=True)
    apellido = models.CharField(max_length=225, blank=False, null=False)
    cedula = models.CharField(max_length=10, blank=False, unique=True)
    direccion = models.TextField(max_length=225, blank=False, null=False)
    celular = models.CharField(max_length=10, blank=False, unique=True) 

    class Meta:
        ordering = ['nombre', 'apellido']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
            return self.nombre + ' ' + self.apellido

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=225, blank=False, unique=True)
    apellido = models.CharField(max_length=225, blank=False, null=False)
    cedula = models.CharField(max_length=10, blank=False, unique=True)
    direccion = models.TextField(max_length=225, blank=False, null=False)
    celular = models.CharField(max_length=10, blank=False, unique=True) 

    class Meta:
        ordering = ['nombre', 'apellido']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

        def __str__(self):
            return self.nombre

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=225, blank=False, unique=True)
    descripcion = models.TextField(max_length=225, blank=False, null=False)
    
    class Meta:
        ordering = ['nombre', 'descripcion']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

        def __str__(self):
            return self.nombre  

def url(self, filename):
    ruta = 'static/img/productos/%s/%s'%(self.nombre, str(filename))
    return ruta 

   
class Producto(models.Model):

    #  def foto_producto(self):
    #     return mark_safe('<a href="/%s"><img src="/%s" width=50px height=50px /></a>'%(self.foto, self.foto))

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=225, blank=False, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)    
    descripcion = models.TextField(max_length=225, blank=False, null=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2) 
    # foto = models.ImageField(upload_to=url)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
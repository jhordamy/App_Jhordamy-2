from django import forms
from.models import *
from django.contrib.auth.models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'celular']
        labels = {
            'nombre': 'Nombres Completos',
            'apellido': 'Apellidos Completos',
            'cedula': 'Cedula de identidad',
            'direccion': 'Direccion',
            'celular': 'Celular',
        }
        Widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '})
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'celular']
        labels = {
            'nombre': 'Nombres Completos',
            'apellido': 'Apellidos Completos',
            'cedula': 'Cedula de identidad',
            'direccion': 'Direccion',
            'celular': 'Celular',
        }
        Widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '})
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombres Completos',
            'descripcion': 'Descripciones',
        }
        Widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '})
        }
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'celular']
        labels = {
            'nombre': 'Nombres Completos',
            'categoria': 'Categorias',
            'proveedor': 'Proveedores',
            'descripcion': 'Descripciones',
            'precio': 'Precios',
        }
        Widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '})
        }
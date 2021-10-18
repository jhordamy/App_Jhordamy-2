from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from.forms import *
from.models import *
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import *

from django.views.generic import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/home/')
        form = LoginForm()
        ctx = {'form': form}
        return render(request, './Login/login.html' , ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def inicio_view(request):
    Jhordamy = Cliente.objects.all()
    ctx = {'Jhordamy': Jhordamy}
    return render(request, 'Login/login.html/', ctx)
     

class CrearCliente(CreateView):
    model = Cliente
    template_name = 'cliente/crearCliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listarCliente')
    
class listarCliente(ListView):
    model = Cliente
    context_object_name = 'cliente/listarCliente.html'
    template_name=ClienteForm
    context_object_name = 'clientes'

class EditarCliente(SuccessMessageMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/editarCliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listarCliente')

@login_required(login_url='/login/')
def inicio_view(request):
    Jhordamy = Proveedor.objects.all()
    ctx = {'Jhordamy': Jhordamy}
    return render(request, 'Login/login.html/', ctx)
     

class CrearProveedor(CreateView):
    model = Proveedor
    template_name = 'proveedor/crearProveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('listarProveedor')
    
class listarPeoveedor(ListView):
    model = Proveedor
    context_object_name = 'proveedor/listarProveedor.html'
    template_name=ProveedorForm
    context_object_name = 'proveedores'

class EditarProveedor(SuccessMessageMixin, UpdateView):
    model = Proveedor
    template_name = 'proveedor/editarProveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('listarProveedor')
    
@login_required(login_url='/login/')
def inicio_view(request):
    Jhordamy = Categoria.objects.all()
    ctx = {'Jhordamy': Jhordamy}
    return render(request, 'Login/login.html/', ctx)
     

class CrearCategoria(CreateView):
    model = Categoria
    template_name = 'categoria/crearCategoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('listarCategoria')
    
class listarCategoria(ListView):
    model = Categoria
    context_object_name = 'categoria/listarCategoria.html'
    template_name=CategoriaForm
    context_object_name = 'categorias'

class EditarCategoria(SuccessMessageMixin, UpdateView):
    model = Categoria
    template_name = 'categoria/editarCategoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('listarCategoria')

@login_required(login_url='/login/')
def inicio_view(request):
    Jhordamy = Producto.objects.all()
    ctx = {'Jhordamy': Jhordamy}
    return render(request, 'Login/login.html/', ctx)
     

class CrearProducto(CreateView):
    model = Producto
    template_name = 'producto/crearProducto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('listarProducto')
    
class listarProductos(ListView):
    model = Producto
    context_object_name = 'producto/listarProducto.html'
    template_name=ProductoForm
    context_object_name = 'productos'

class EditarProducto(SuccessMessageMixin, UpdateView):
    model = Producto
    template_name = 'producto/editarProducto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('listarProducto')
    
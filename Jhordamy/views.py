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
from django.views.decorators.csrf import csrf_protect
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import *

# Create your views here.
# @csrf_protect
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


@login_required(login_url='/')
def inicio_view(request):
    return render(request, 'base.html')

class crearCliente(CreateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'Cliente/crearCliente.html'
    success_url = reverse_lazy('listar')

class listarCliente(ListView):
    model = Cliente
    template_name = 'Cliente/listarCliente.html'
    context_object_name = 'clientes'

class editarCliente(SuccessMessageMixin, UpdateView):
    model = Cliente
    template_name = 'Cliente/editarCliente.html'
    form_class = clienteFormEdit
    success_url = reverse_lazy('listar')

# class CrearProveedor(CreateView):
#     model = Proveedor
#     template_name = 'proveedor/crearProveedor.html'
#     form_class = ProveedorForm
#     success_url = reverse_lazy('listarProveedor')
    
# class listarPeoveedor(ListView):
#     model = Proveedor
#     context_object_name = 'proveedor/listarProveedor.html'
#     template_name=ProveedorForm
#     context_object_name = 'proveedores'

# class EditarProveedor(SuccessMessageMixin, UpdateView):
#     model = Proveedor
#     template_name = 'proveedor/editarProveedor.html'
#     form_class = ProveedorForm
#     success_url = reverse_lazy('listarProveedor')

# class CrearCategoria(CreateView):
#     model = Categoria
#     template_name = 'categoria/crearCategoria.html'
#     form_class = CategoriaForm
#     success_url = reverse_lazy('listarCategoria')
    
# class listarCategoria(ListView):
#     model = Categoria
#     context_object_name = 'categoria/listarCategoria.html'
#     template_name=CategoriaForm
#     context_object_name = 'categorias'

# class EditarCategoria(SuccessMessageMixin, UpdateView):
#     model = Categoria
#     template_name = 'categoria/editarCategoria.html'
#     form_class = CategoriaForm
#     success_url = reverse_lazy('listarCategoria')

# class CrearProducto(CreateView):
#     model = Producto
#     template_name = 'producto/crearProducto.html'
#     form_class = ProductoForm
#     success_url = reverse_lazy('listarProducto')
    
# class listarProductos(ListView):
#     model = Producto
#     context_object_name = 'producto/listarProducto.html'
#     template_name=ProductoForm
#     context_object_name = 'productos'

# class EditarProducto(SuccessMessageMixin, UpdateView):
#     model = Producto
#     template_name = 'producto/editarProducto.html'
#     form_class = ProductoForm
#     success_url = reverse_lazy('listarProducto')

# ************************************************************** DJANGO REST FRAMEWORK ***************

class clienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer

class productoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer

class proveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = proveedorSerializer

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer
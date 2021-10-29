from django.contrib import admin
from django.urls import path,include
from Jhordamy.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [

    # URLS PRINCIPALES
    path('admin/', admin.site.urls),
    path('', include('Jhordamy.urls')),
    path('', login_view, name='view_login'),
    path('home/', inicio_view, name='vista_inicio'),
    path('logout/', logout_view, name='view_logout'),
    path('listar/',login_required(listarCliente.as_view()), name='listar'),
    path('nuevoC/',login_required(CrearCliente.as_view()), name='nuevoCliente'),

    path('listar/',login_required(listarPeoveedor.as_view()), name='listar'),
    path('listar/',login_required(listarPeoveedor.as_view()), name='listar'),
    path('listar/',login_required(listarCategoria.as_view()), name='listar'),
    path('listar/',login_required(listarProductos.as_view()), name='listar'),



    # API-REST
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path ('listaCliente/', login_required(listarCliente.as_view()), name = 'listarCliente'),
    #path('crearCliente/', login_required(CrearCliente.as_view()), name = 'crearCliente'),
    #path('editarCliente/<init:pk>/', login_required(EditarCliente.as_view()), name = 'editarCliente'),
    
]
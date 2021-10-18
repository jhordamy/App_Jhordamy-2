from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from Jhordamy.views import CrearCliente, EditarCliente, inicio_view, listarCliente, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Jhordamy.urls')),
    path('', login_view, name="vista_login"),
    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    
     #================ URL BASADA EN CLASES Y FUNCIONES ==============#
    path('listarCliente/', login_required(listarCliente.as_view()), name='listarCliente'),
    path('crearCliente/', login_required(CrearCliente.as_view()), name='crearCliente'),
    path('editarCliente/<int: pk>/',login_required(EditarCliente.as_view()), name='editarCliente'), 
    

]
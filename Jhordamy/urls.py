from django.urls import include, path

from .views import *

from . import views

from rest_framework import routers, permissions

router = routers.DefaultRouter()
# Necesita un basename ya que no le especificamos en la vista
router.register('clientes', views.clienteViewSet)
router.register('proveedores', views.proveedorViewSet)
router.register('categorias', views.categoriaViewSet)
router.register('productos', views.productoViewSet)

urlpatterns = [
    # URLS PRINCIPALES
    path('', login_view, name='view_login'),
    path('home/', inicio_view, name='view_home'),
    path('logout/', logout_view, name='view_logout'),
    # URLS CLIENTES
    path('home/listar_clientes/',login_required(listarCliente.as_view()),name='listar'),
    path('home/crear_cliente/',login_required(crearCliente.as_view()),name='crear_cliente'),
    path('home/editar_cliente/<int:pk>/',login_required(editarCliente.as_view()),name='editar_cliente'),
    # API-REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

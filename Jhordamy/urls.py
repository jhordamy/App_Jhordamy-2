
from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/clientes',ClienteViewset)
router.register('api/proveedores',ProveedorViewset)
router.register('api/productos',ProductoViewset)
router.register('api/categorias',CategoriaViewset)
urlpatterns = router.urls
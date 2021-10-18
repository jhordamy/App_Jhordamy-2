
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Jhordamy.urls')),
]

admin.site.site_header = 'ADMINISTRACION JHORDAMY'


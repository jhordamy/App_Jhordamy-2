from django.urls import include, path

from .views import *

urlpatterns = [
    # URLS PRINCIPALES
    path('', login_view, name='view_login'),
    path('home/', inicio_view, name='view_home'),
    path('logout/', logout_view, name='view_logout'),
    # API-REST
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
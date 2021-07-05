"""CakeHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pasteleria.models import Dato
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from CakeHouse import views



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'datos', views.DatoViewSet)
router.register(r'compras', views.CompraViewSet)
router.register(r'tipo_de_productos',views.Tipo_de_productoViewSet)

urlpatterns = [

    path('pasteleria/', include('pasteleria.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

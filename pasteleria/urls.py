from os import name
from django.urls import path

from . import views

app_name = 'pasteleria'
urlpatterns = [

    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('inicio',views.inicio, name='inicio'),
    path('indexReturn',views.indexReturn, name='indexReturn'),
    path('validación',views.validación, name='validación'),
    path('producto',views.producto, name='producto'),
    path('producto1',views.producto1, name='producto1'),
    path('producto2',views.producto2, name='producto2'),
    path('pago',views.pago,name='pago'),
    path('pago1',views.pago1,name='pago1'),
    path('pago2',views.pago2,name='pago2'),
    path('descuento',views.descuento,name='descuento'),
    path('descuento1',views.descuento1,name='descuento1'),
    path('descuento2',views.descuento2,name='descuento2'),
    path('pastel',views.pastel,name='pastel'),
    path('pastel1',views.pastel1,name='pastel1'),
    path('pastel2',views.pastel2,name='pastel2'),
    path('rebaja',views.rebaja,name='rebaja'),
    path('editar',views.editar,name='editar'),
    path('editar_usuario',views.editar_usuario,name='editar_usuario'),
    path('actualizar_usuario',views.actualizar_usuario,name='actualizar_usuario'),
    path('eliminar_usuario',views.eliminar_usuario,name='eliminar_usuario'),
    path('eliminar_datos',views.eliminar_datos,name='eliminar_datos'),

]

from pasteleria.models import Compra, Dato, Tipo_de_producto
from rest_framework import serializers


class DatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dato
        fields = ['url' ,'id', 'rut', 'Nombre', 'Apellido', 'Gmail', 'telefono']

class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ['url', 'tipo_producto', 'id', 'Cantidad_de_Personas', 'Cantidad_de_Tortas', 'precio']

class Tipo_de_productoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_de_producto
        fields = ['url', 'id', 'nombre']
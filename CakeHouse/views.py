from pasteleria.models import Compra, Dato, Tipo_de_producto
from rest_framework import viewsets
from rest_framework import permissions
from CakeHouse.serializers import CompraSerializer, DatoSerializer, Tipo_de_productoSerializer

class DatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dato.objects.all()
    serializer_class = DatoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [permissions.IsAuthenticated]

class Tipo_de_productoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tipo_de_producto.objects.all()
    serializer_class = Tipo_de_productoSerializer
    permission_classes = [permissions.IsAuthenticated]



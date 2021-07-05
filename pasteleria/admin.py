from django.contrib import admin
from .models import Compra, Tipo_de_producto,Dato
# Register your models here.

admin.site.register(Tipo_de_producto)
admin.site.register(Compra)
admin.site.register(Dato)
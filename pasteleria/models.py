from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext as _


# Create your models here.
class Tipo_de_producto(models.Model):
    nombre = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    tipo_producto = models.ForeignKey(Tipo_de_producto, on_delete=models.CASCADE)
    Cantidad_de_Personas = models.CharField(max_length=20,default='')
    Cantidad_de_Tortas = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField('Fecha de creación')
    precio = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.tipo_producto)


class Dato(models.Model):
  
    rut = models.CharField(max_length=12,default='')
    Nombre = models.CharField(max_length=20,default='')
    Apellido = models.CharField(max_length=20,default='')
    Gmail = models.CharField(max_length=100,default='')
    telefono = models.CharField(max_length=12,default='')
    contraseña = models.CharField(max_length=20,default='')
    fecha_creacion = models.DateTimeField('Fecha de creación')

    def __str__(self):
        return self.rut

    class Meta:
        permissions = (

            ('usuario', _('es usuario')),

        )
       

    
        

        
    

   
    


        

from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.shortcuts import render
from rest_framework.permissions import AND
from pasteleria.models import Compra,Tipo_de_producto,Dato
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def index(request):
   if request.user.has_perm('pasteleria.usuario'):
      return render(request,'pasteleria/Login.html')
   else:
      return HttpResponse('No tiene los permisos para logearse')

def validación(request):
   Rut = request.POST['rut']
   Contraseña = request.POST['Contraseña']

   if Dato.objects.filter(rut = request.POST['rut']):
      if Dato.objects.filter(contraseña = request.POST['Contraseña']):
         return render(request,'pasteleria/inicio.html')
      else:
         return HttpResponse('Contraseña incorrecta o no existe')
   else:
      return HttpResponse('El rut no existe o es incorrecto')
   

   
   
def indexReturn(request):
   Nombre = request.POST['Nombre']
   Apellido = request.POST['Apellido']
   Rut = request.POST['rut']
   Contraseña = request.POST['Contraseña']
   Correo = request.POST['Correo']
   Telefono = request.POST['Telefono']
   fecha_creacion = timezone.now()
   Usuario = Dato(rut=Rut,Nombre=Nombre,Apellido=Apellido,Gmail=Correo,contraseña=Contraseña,telefono=Telefono,fecha_creacion=fecha_creacion)
   Usuario.save()
   return HttpResponseRedirect(reverse('pasteleria:index'))

def pastel(request):
   limite = request.POST.get('personas')
   Cantidad = request.POST.get('cantidad')
   id_producto = 4
   tipoProducto = Tipo_de_producto(id=id_producto)
   fecha_actual = timezone.now()
   Precio = 10000
   

   compra = Compra(Cantidad_de_Personas=int(limite),tipo_producto=tipoProducto,Cantidad_de_Tortas=int(Cantidad),fecha_creacion=fecha_actual,precio=Precio)
   compra.save()
   return render(request,'pasteleria/pago.html')


def pastel1(request):
   limite = request.POST.get('personas')
   Cantidad = request.POST.get('cantidad')
   id_producto = 3
   tipoProducto = Tipo_de_producto(id=id_producto)
   fecha_actual = timezone.now()
   Precio = 25000
   

   compra = Compra(Cantidad_de_Personas=int(limite),tipo_producto=tipoProducto,Cantidad_de_Tortas=int(Cantidad),fecha_creacion=fecha_actual,precio=Precio)
   compra.save()
   return render(request,'pasteleria/pago1.html')

def pastel2(request):
   limite = request.POST.get('personas')
   Cantidad = request.POST.get('cantidad')
   id_producto = 2
   tipoProducto = Tipo_de_producto(id=id_producto)
   fecha_actual = timezone.now()
   Precio = 20000
   

   compra = Compra(Cantidad_de_Personas=int(limite),tipo_producto=tipoProducto,Cantidad_de_Tortas=int(Cantidad),fecha_creacion=fecha_actual,precio=Precio)
   compra.save()
   return render(request,'pasteleria/pago2.html')



def editar(request):
   carro = Dato.objects.order_by('-fecha_creacion')[:5]
   context = {'listado': carro}
   return render(request,'pasteleria/editar.html',context)

def editar_usuario(request):
   return render(request,'pasteleria/editar_usuario.html')

def actualizar_usuario(request):
   fecha_actualizacion = timezone.now()

   if request.POST['Nombre'] != '' or request.POST['Apellido'] != '' or request.POST['Correo'] != '' or request.POST['Telefono'] != '' or request.POST['Contraseña'] != '':
      if Dato.objects.filter(rut = request.POST['rut']):
         Dato.objects.update(
         Nombre=request.POST['Nombre'],
         Apellido=request.POST['Apellido'],
         Gmail=request.POST['Correo'],
         telefono=request.POST['Telefono'],
         contraseña=request.POST['Contraseña'],
         fecha_creacion=fecha_actualizacion)
         return render(request,'pasteleria/Login.html')
      else:
         return HttpResponse('El rut tiene que ser correcto o existir para cambiar los datos personales')
   else:
      return HttpResponse('Tiene que llenar los campos correspondientes')

def eliminar_usuario(request):
   return render(request, 'pasteleria/eliminar_usuario.html')

def eliminar_datos(request):
   
   if Dato.objects.filter(rut=request.POST['rut']):
      Dato.objects.filter(rut=request.POST['rut']).delete()
      return render(request, 'pasteleria/Login.html')
   else:
      return HttpResponse('El rut no existe o es incorrecto')

   


def registro(request):
   return render(request,'pasteleria/registro1.html')

def inicio(request):
   return render (request, 'pasteleria/inicio.html')

def producto(request):
   return render (request,'pasteleria/producto.html')

def producto1(request):
   return render (request,'pasteleria/producto1.html')

def producto2(request):
   return render (request,'pasteleria/producto2.html')

def pago(request):
   return render (request, 'pasteleria/pago.html')

def pago1(request):
   return render (request, 'pasteleria/pago1.html')

def pago2(request):
   return render (request, 'pasteleria/pago2.html')

def descuento(request):

   
  

   Precio = 10000
   if Compra.objects.filter(precio = Precio) and Compra.objects.latest('fecha_creacion'):
      Compra.objects.update(precio = 8500)
      return render(request, 'pasteleria/descuento.html')
   else:
      return HttpResponse('No realizó bien su compra')
   

def descuento1(request):

   Precio = 25000
   if Compra.objects.filter(precio = Precio) and Compra.objects.latest('fecha_creacion'):
      Compra.objects.update(precio = 21250)
      return render(request, 'pasteleria/descuento1.html')
   else:
      return HttpResponse('No realizó bien su compra')

def descuento2(request):

   
   Precio = 20000
   if Compra.objects.filter(precio = Precio) and Compra.objects.latest('fecha_creacion'):
      Compra.objects.update(precio = 17000)
      return render(request, 'pasteleria/descuento2.html')
   else:
      return HttpResponse('No realizó bien su compra')

def rebaja(request):
   
   return render(request, 'pasteleria/inicio.html')

   
   
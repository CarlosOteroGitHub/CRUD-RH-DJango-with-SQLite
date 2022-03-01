from django.shortcuts import render, redirect
from .models import Empleado
from django.contrib import messages

# Create your views here.
def home(request):
	empleados_listado = Empleado.objects.all()
	messages.success(request, '¡Empleados listados!')
	return render(request, "empleado.html", {"empleados": empleados_listado})

#PROCESO PARA INSERTAR EN LA BASE DE DATOS.
def insertarEmpleado(request):
	id_empleado=request.POST['txtID']
	nombre=request.POST['txtNombre']
	nacimiento=request.POST['txtNacimiento']
	descripcion=request.POST['txtDescripcion']

	empleado = Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, nacimiento=nacimiento, descripcion=descripcion)
	messages.success(request, '¡Empleado Agregado!')

	return redirect('/')

#PROCESO PARA REFERENCIAR A LA VISTA DE EDICIÓN CON LOS DATOS DEL REGISTRO.
def edicionEmpleado(request, id_empleado):
	empleado = Empleado.objects.get(id_empleado=id_empleado)
	return render(request, "editar.html", {"empleado": empleado})	

#PROCESO PARA EDITAR EN LA BASE DE DATOS.
def editarEmpleado(request):
	id_empleado=request.POST['txtID']
	nombre=request.POST['txtNombre']
	nacimiento=request.POST['txtNacimiento']
	descripcion=request.POST['txtDescripcion']

	empleado = Empleado.objects.get(id_empleado=id_empleado)
	empleado.id_empleado = id_empleado
	empleado.nombre = nombre
	empleado.nacimiento = nacimiento
	empleado.descripcion = descripcion
	empleado.save()

	messages.success(request, '¡Empleado Editado!')

	return redirect('/')

#PROCESO PARA ELIMINAR EN LA BASE DE DATOS.
def eliminarEmpleado(request, id_empleado):
	empleado = Empleado.objects.get(id_empleado=id_empleado)
	empleado.delete()

	messages.success(request, '¡Empleado Eliminado!')
	
	return redirect('/')
from django.urls import path
from . import views

#PROCESO PARA DIRECCIONAR A LAS VISTAS.
urlpatterns = [
	path('', views.home),
	path('insertarEmpleado/', views.insertarEmpleado),
	path('edicionEmpleado/<id_empleado>', views.edicionEmpleado),
	path('editarEmpleado/', views.editarEmpleado),
	path('eliminarEmpleado/<id_empleado>', views.eliminarEmpleado),
]
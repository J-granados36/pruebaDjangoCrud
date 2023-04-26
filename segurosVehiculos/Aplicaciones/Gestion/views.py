from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def home(request):
    empleadosListados = Empleado.objects.all() #Listar
    return render(request, "gestionEmpleados.html",{"empleados": empleadosListados})

def registrarEmpleado(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    telefono=request.POST['txtTelefono']
    cedula=request.POST['numCedula']
    correo =request.POST['txtCorreo']
    
    empleado = Empleado.objects.create(
        codigo=codigo, nombre=nombre, telefono=telefono, cedula=cedula, correo=correo)
    return redirect('/')

def edicionEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "edicionEmpleado.html", {"empleado":empleado})

def editarEmpleado(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    telefono=request.POST['txtTelefono']
    cedula=request.POST['numCedula']
    correo =request.POST['txtCorreo']
    
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre = nombre
    empleado.telefono = telefono
    empleado.cedula = cedula
    empleado.correo = correo
    empleado.save()
    
    return redirect('/')

def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('/')
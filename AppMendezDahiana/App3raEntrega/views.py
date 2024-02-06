from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, "APP3raEntrega/inicio.html")

def tratamientos(request):
    contexto = {'tratamientos': Tratamiento.objects.all()}
    return render(request, "APP3raEntrega/tratamientos.html", contexto)

def personal(request):
    contexto = {'personal': Personal.objects.all()}
    return render(request, "APP3raEntrega/personal.html", contexto)

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "APP3raEntrega/clientes.html", contexto)

def tratamiento_formulario(request):
    if request.method == 'POST':
        mi_formulario = Tratamiento_Formulario(request.POST)
        if mi_formulario.is_valid():
            tratamiento_nombre = mi_formulario.cleaned_data.get("nombre")
            tratamiento_descripcion = mi_formulario.cleaned_data.get("descripcion")
            tratamiento_precio = mi_formulario.cleaned_data.get("precio")
            tratamiento_duracion = mi_formulario.cleaned_data.get("duracion")
            tratamiento = Tratamiento(nombre=tratamiento_nombre, descripcion=tratamiento_descripcion, precio=tratamiento_precio, duracion=tratamiento_duracion)
            tratamiento.save()
        return render(request, "App3raEntrega/inicio.html")    
    else:
        mi_formulario = Tratamiento_Formulario()
    return render(request, "App3raEntrega/tratamiento_formulario.html", {"mi_formulario": mi_formulario})

def personal_formulario(request):
    if request.method == 'POST':
        mi_formulario = Personal_Formulario(request.POST)
        if mi_formulario.is_valid():
            personal_nombre = mi_formulario.cleaned_data.get("nombre")
            personal_apellido = mi_formulario.cleaned_data.get("apellido")
            personal_especialidad  = mi_formulario.cleaned_data.get("especialidad")
            personal = Personal(nombre=personal_nombre, apellido=personal_apellido, especialidad=personal_especialidad)
            personal.save()
        return render(request, "App3raEntrega/inicio.html")
    else:
        mi_formulario = Personal_Formulario()
    return render(request, "App3raEntrega/personal_formulario.html", {"mi_formulario": mi_formulario})

def cliente_formulario(request):
    if request.method == 'POST':
        mi_formulario = Cliente_Formulario(request.POST)
        if mi_formulario.is_valid():
            cliente_nombre = mi_formulario.cleaned_data.get("nombre")
            cliente_apellido = mi_formulario.cleaned_data.get("apellido")
            cliente_telefono = mi_formulario.cleaned_data.get("telefono")
            cliente_correo = mi_formulario.cleaned_data.get("correo_electronico")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, telefono=cliente_telefono, correo_electronico=cliente_correo)
            cliente.save()
        return render(request, "App3raEntrega/inicio.html")
    else:
        mi_formulario = Cliente_Formulario()
    return render(request, "App3raEntrega/cliente_formulario.html", {"mi_formulario": mi_formulario})

def buscar(request):
    return render(request, "App3raEntrega/buscar.html")


def buscar_tratamientos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        tratamientos = Tratamiento.objects.filter(nombre__icontains=patron)
        contexto = {"tratamientos": tratamientos}
        return render(request, "App3raEntrega/tratamientos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda, vuelva a intentarlo")

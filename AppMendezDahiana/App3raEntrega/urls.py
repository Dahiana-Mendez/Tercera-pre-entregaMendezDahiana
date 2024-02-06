from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('tratamientos', tratamientos, name="tratamientos"),
    path('personal', personal, name="personal"),
    path('clientes', clientes, name="clientes"),
    #
    path('tratamiento_formulario', tratamiento_formulario, name="tratamiento_formulario"),
    path('personal_formulario', personal_formulario, name="personal_formulario"),
    path('cliente_formulario', cliente_formulario, name="cliente_formulario"), 
    path('buscar/', buscar, name="buscar"),
    path('buscar_tratamientos/', buscar_tratamientos, name="buscar_tratamientos"),
]
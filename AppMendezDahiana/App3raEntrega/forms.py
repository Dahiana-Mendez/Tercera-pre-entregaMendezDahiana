from django import forms

class Tratamiento_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    descripcion = forms.CharField(max_length=200, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    duracion = forms.IntegerField(required=True)

class Personal_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    apellido = forms.CharField(max_length=200, required=True)
    especialidad = forms.CharField(max_length=100, required=True)

class Cliente_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    apellido = forms.CharField(max_length=200, required=True)
    telefono = forms.CharField(max_length=20, required=True)
    correo_electronico = forms.EmailField(required=True)

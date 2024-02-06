from django.db import models

# Create your models here.
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}"
     
class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Empleados"

    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.telefono}"

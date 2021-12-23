from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
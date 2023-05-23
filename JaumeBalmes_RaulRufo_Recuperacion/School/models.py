from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    segundoApellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()

#
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    segundoApellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    imparte =  models.BooleanField(default=True)



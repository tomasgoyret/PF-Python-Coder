from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    rol = models.CharField(max_length=50, default = None)
    apellido = models.CharField(max_length=50, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    edad = models.IntegerField(default = None)
class SegundosFamiliares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    rol = models.CharField(max_length=50, default = None)
    apellido = models.CharField(max_length=50, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    edad = models.IntegerField(default = None)
class BienesFamiliares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    valuacion = models.IntegerField(default = None)
    antigüedad = models.IntegerField(default = None)




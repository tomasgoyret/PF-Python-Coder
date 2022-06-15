from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    rol = models.CharField(max_length=50, default = None)
    apellido = models.CharField(max_length=50, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    edad = models.IntegerField(default = None)
    def __str__(self):
        return f'{self.nombre}+" "+str{self.apellido}" "+str{self.rol}+str{self.fechaDeNacimiento}" "+str{self.edad}'
class SegundosFamiliares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    rol = models.CharField(max_length=50, default = None)
    apellido = models.CharField(max_length=50, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    edad = models.IntegerField(default = None)
    def __str__(self):
        return f'{self.nombre}+" "+str{self.apellido}" "+str{self.rol}+str{self.fechaDeNacimiento}" "+str{self.edad}'
class BienesFamiliares(models.Model):
    nombre = models.CharField(max_length=50, default = None)
    valuacion = models.IntegerField(default = None)
    antigüedad = models.IntegerField(default = None)
    def __str__(self):
        return f'{self.nombre}+" "+Valuacion{self.valuacion}+Antugüedad{self.antigüedad}'



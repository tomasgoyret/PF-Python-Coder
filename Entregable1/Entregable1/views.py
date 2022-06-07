from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context 
from django.template import loader
from EntregableApp.models import Familiares 

def familia_template(self):
    familiar = Familiares(nombre="Tomas", apellido="Langeneker", fechaDeNacimiento = "2003-07-18", edad = 18 )
    familiar.save()
    diccionario = {"familiar":familiar}
    
    familiar1 = Familiares(nombre="Ian", apellido="Langeneker", fechaDeNacimiento = "2000-09-01", edad = 21 )
    familiar1.save()
    diccionario["familiar1"] = familiar1
    
    familiar2 = Familiares(nombre="Marcelo", apellido="Langeneker", fechaDeNacimiento = "1965-02-19", edad = 57 )
    familiar2.save()
    diccionario["familiar2"] = familiar2
    
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


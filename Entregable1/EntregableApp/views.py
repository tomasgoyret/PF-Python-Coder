from django.shortcuts import render
from EntregableApp.models import Familiares
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from EntregableApp.models import Familiares, BienesFamiliares, SegundosFamiliares
from EntregableApp.forms import FamiliaresFormulario, BienesFormulario, Familiares_SegundosFormulario

def inicio(request):
    plantilla = loader.get_template('EntregableApp/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
    
def familia(request):
    familiares = Familiares.objects.all()
    contexto = {'familiares' : familiares}
    plantilla = loader.get_template('EntregableApp/familia.html')
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def bienes(request):
    bienes = BienesFamiliares.objects.all()
    contexto = {'bienes' : bienes}
    plantilla = loader.get_template('EntregableApp/bienes.html')
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def familia_segunda(request):
    segundosfamiliares = SegundosFamiliares.objects.all()
    contexto = {'segundosfamiliares' : segundosfamiliares }
    plantilla = loader.get_template('EntregableApp/familia_segunda.html')
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
   
    
def familiaformulario(request):
    if request.method == 'POST':
        miFormulario = FamiliaresFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        rol = informacion['rol']
        fechaDeNacimiento = informacion['fechaDeNacimiento']
        edad = informacion['edad']
        familia = Familiares(nombre=nombre,apellido=apellido,rol=rol,edad=edad,fechaDeNacimiento=fechaDeNacimiento)
        familia.save()
        return render(request,'EntregableApp/inicio.html')
    else:
        miFormulario = FamiliaresFormulario()
    return render(request,'EntregableApp/familiaformulario.html', {"miFormulario":miFormulario})
def bienesformulario(request):
    if request.method == 'POST':
        miFormulario = BienesFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        valuacion = informacion['valuacion']
        antigüedad = informacion['antigüedad']
        bienes = BienesFamiliares(nombre=nombre,valuacion=valuacion,antigüedad=antigüedad)
        bienes.save()
        return render(request,'EntregableApp/inicio.html')
    else:
        miFormulario = BienesFormulario()
    return render(request,'EntregableApp/bienesformulario.html', {"miFormulario":miFormulario})

def familia_segundaformulario(request):
    if request.method == 'POST':
        miFormulario = Familiares_SegundosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        rol = informacion['rol']
        fechaDeNacimiento = informacion['fechaDeNacimiento']
        edad = informacion['edad']
        familia = Familiares_SegundosFormulario(nombre=nombre,apellido=apellido,rol=rol,edad=edad,fechaDeNacimiento=fechaDeNacimiento)
        familia.save()
        return render(request,'EntregableApp/inicio.html')
    else:
        miFormulario = Familiares_SegundosFormulario()
    return render(request,'EntregableApp/familia_segundaformulario.html', {"miFormulario":miFormulario})
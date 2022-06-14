from django.shortcuts import render
from EntregableApp.models import Familiares
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from EntregableApp.models import Familiares, BienesFamiliares, SegundosFamiliares
from EntregableApp.forms import FamiliaresFormulario, BienesFormulario

def inicio(request):
    plantilla = loader.get_template('EntregableApp/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
    
def familia(request):
    plantilla = loader.get_template('EntregableApp/familia.html')
    documento = plantilla.render()
    return HttpResponse(documento)
def bienes(request):
    return render(request, 'EntregableApp/bienes.html')
def familia_segunda(request):
    return render(request, 'EntregableApp/familia_segunda.html')
    
def familiaformulario(request):
    if request.method == 'POST':
        miFormulario = FamiliaresFormulario(request.POST)
        print(miFormulario)
        print("mirar aca")
        if miFormulario.is_valid:
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
        print(miFormulario)
        if miFormulario.is_valid:
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
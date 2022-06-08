from django.shortcuts import render
from EntregableApp.models import Familiares
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from EntregableApp.models import Familiares, BienesFamiliares, SegundosFamiliares

def inicio(request):
    return render(request, 'EntregableApp/inicio.html')
def familia(request):
    return render(request, 'EntregableApp/familia.html')
def bienes(request):
    return render(request, 'EntregableApp/bienes.html')
def familia_segunda(request):
    return render(request, 'EntregableApp/familia_segunda.html')
    

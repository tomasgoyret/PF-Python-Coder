from django.shortcuts import render
from EntregableApp.models import Familiares
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from EntregableApp.models import Familiares 

def inicio(request):
    return render(request, 'inicio.html')

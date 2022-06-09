from django.urls import path
from EntregableApp import views
from .views import inicio, bienes, familia, familia_segunda, familiaformulario, bienesformulario
urlpatterns = [
    path("inicio", views.inicio, name="inicio" ),
    path("bienes", views.bienes, name="bienes"),
    path("familia", views.familia, name="familia"),
    path("familiaSegunda", views.familia_segunda, name="familiaSegunda"),
    path("familiaFormulario", views.familiaformulario, name="familiaFormulario"),
    path("bienesformulario", views.bienesformulario, name="bienesformulario"),
]
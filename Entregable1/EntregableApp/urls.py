from django.urls import path
from EntregableApp import views
from .views import inicio, bienes, familia, familia_segunda
urlpatterns = [
    path("", views.inicio),
    path("bienes", views.bienes),
    path("familia", views.familia),
    path("familiaSegunda", views.familia_segunda),
]
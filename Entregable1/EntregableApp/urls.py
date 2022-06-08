from django.urls import path
from EntregableApp import views
from .views import inicio
urlpatterns = [
    path("", views.inicio),
]
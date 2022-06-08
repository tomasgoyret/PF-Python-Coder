from django.contrib import admin
from django.urls import path, include
from Entregable1.views import familia_template
urlpatterns = [
    path('admin/', admin.site.urls),
    path("EntregableApp/", include("EntregableApp.urls")),
]

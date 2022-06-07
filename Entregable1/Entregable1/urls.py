from django.contrib import admin
from django.urls import path
from Entregable1.views import familia_template
urlpatterns = [
    path('admin/', admin.site.urls),
    path("familiares/", familia_template),
]

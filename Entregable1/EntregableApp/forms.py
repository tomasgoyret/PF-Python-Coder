from django import forms


class FamiliaresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_De_Nacimiento= forms.DateField()
    edad = forms.IntegerField()
    rol = forms.CharField()
class BienesFormulario(forms.Form):
    nombre = forms.CharField()
    valuacion = forms.CharField()
    antigüedad = forms.IntegerField()
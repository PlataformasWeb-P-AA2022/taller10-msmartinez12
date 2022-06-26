from django.forms import ModelForm
from django import forms

from ordenamiento.models import *

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo_parroquia'] 

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia'] 
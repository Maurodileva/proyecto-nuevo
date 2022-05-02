from msilib.schema import Class
from django import forms

class CalzadoFormulario(forms.Form):

    marca = forms.CharField()
    talle = forms.IntegerField()
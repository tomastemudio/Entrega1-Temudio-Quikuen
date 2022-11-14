from django import forms 
from ckeditor.fields import RichTextFormField

class Jugador(forms.Form):
    nombre = forms.CharField(max_length = 30)
    apellido = forms.CharField(max_length = 30)
    nacionalidad = forms.CharField(max_length = 30)
    liga = forms.CharField(max_length = 30)
    fechacrracion = forms.DateField()
    descripcion = RichTextFormField(required=False)

class BusquedaJugador(forms.Form):
    apellido = forms.CharField(max_length = 30, required=False)
        
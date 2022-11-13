from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import CharField

class CreacionUsuario(UserCreationForm):
    email = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class EditarPerfil(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    avatar = forms.ImageField(required=False)
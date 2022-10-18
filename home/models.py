from django.db import models
from django.forms import CharField
# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    nacionalidad = models.CharField(max_length = 30)
    liga = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.nombre} {self.apellido}; nacionalidad: {self.nacionalidad}; liga: {self.liga}'
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField
#from ckeditor import Rc
# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    nacionalidad = models.CharField(max_length = 30)
    liga = models.CharField(max_length = 30)
    fechacrracion = models.DateField()
    descripcion = RichTextField(null=True)
    def __str__(self):
        return f'''Juagdor -- > {self.nombre} {self.apellido}. 
                 Nacionalidad --> {self.nacionalidad}.
                 Liga --> {self.liga}.
                 Fecha De Creracion  --> {self.fechacrracion}.'''
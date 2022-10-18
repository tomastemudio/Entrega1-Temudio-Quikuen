from django.shortcuts import render
from home.models import Jugador
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class VerJugador(ListView):
    model = Jugador
    template_name = 'home/ver_jugador.html'    

class CrearJugador(CreateView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/crear_jugador.html'
    fields = ['nombre', 'apellido', 'nacionalidad', 'liga']

class EditarJugador(UpdateView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/editar_jugador.html'
    fields = ['nombre', 'apellido', 'nacionalidad', 'liga']

class EliminarJugador(DeleteView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/eliminar_jugador.html'

def index(request):
    return render(request, 'home/index.html')

def sobre_nosotros(request):
    return render(request, 'home/sobre_nosotros.html')
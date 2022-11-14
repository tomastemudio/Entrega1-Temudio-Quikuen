from django.shortcuts import render
from home.models import Jugador
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from home.forms import BusquedaJugador
# Create your views here.

class VerJugador(ListView):
    model = Jugador
    template_name = 'home/ver_jugador.html'    

    def get_queryset(self):
        apellido = self.request.GET.get('apellido','')
        if apellido:
            object_list = self.model.objects.filter(apellido_icontains = apellido)
        else: 
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaJugador()
        return context

class VerUnJudador (DeleteView):
    model = Jugador
    template_name = 'home/ver_unjugador.html'
    

class CrearJugador(CreateView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/crear_jugador.html'
    fields = ['nombre', 'apellido', 'nacionalidad', 'liga', 'descripcion']


class EditarJugador(UpdateView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/editar_jugador.html'
    fields = ['nombre', 'apellido', 'nacionalidad', 'liga', 'descripcion']


class EliminarJugador(DeleteView):
    model = Jugador
    success_url = '/jugador/'
    template_name = 'home/eliminar_jugador.html'


def index(request):
    return render(request, 'home/index.html')

def sobre_nosotros(request):
    return render(request, 'home/sobre_nosotros.html')
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugador/', views.VerJugador.as_view(), name = 'ver_jugador'),
    path('jugador/crear', views.CrearJugador.as_view(), name = 'crear_jugador'),
    path('jugador/editar/<int:pk>', views.EditarJugador.as_view(), name = 'editar_jugador'),
    path('jugador/ver/', views.VerUnJudador.as_view(), name = 'ver_unjugador'),
    path('jugador/eliminar/<int:pk>', views.EliminarJugador.as_view(), name = 'eliminar_jugador'),
    path('jugador/sobre-nosotros', views.sobre_nosotros, name = 'sobre_nosotros')
]
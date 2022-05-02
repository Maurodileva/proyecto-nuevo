from unicodedata import name
from django.urls import path
from .views import buscar, busquedaCalzado, calzadoFormulario, inicio
from proyecto1.views import pruebaTemplate

from proyecto1.views import prueba
from .views import calzado
from .views import remera
from .views import pantalon

urlpatterns = [
    path('', inicio, name = 'Inicio' ),
    path('prueba/', prueba),
    path('pruebaTemplate/<nombre>', pruebaTemplate),
    path('nuevoCalzado/', calzado, name = 'Calzado'),
    path('nuevaRemera/', remera, name = 'Remera'),
    path('nuevoPantalon/', pantalon, name = 'Pantalon'),
    path('calzadoFormulario/', calzadoFormulario, name = 'CalzadoFormulario'),
    path('busquedaCalzado/', busquedaCalzado, name = 'BusquedaCalzado'),
    path('buscar/', buscar, name = 'Buscar'),
]
from django.urls import path
from .views import inicio
from proyecto1.views import pruebaTemplate

from proyecto1.views import prueba
from .views import calzado
from .views import remera
from .views import pantalon

urlpatterns = [
    path('', inicio),
    path('prueba/', prueba),
    path('pruebaTemplate/<nombre>', pruebaTemplate),
    path('nuevoCalzado/<marca>/<talle>', calzado),
    path('nuevaRemera/<marca>/<talle>/<color>', remera),
    path('nuevoPantalon/<marca>/<talle>/<tipo_de_tela>', pantalon),
]
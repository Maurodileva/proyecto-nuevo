from django.http import HttpResponse
from django.shortcuts import render

from .forms import CalzadoFormulario
from .models import Calzado, Pantalon, Remera
# Create your views here.

def calzado(request):

    return render(request,"Atuendos/calzado.html") 

def remera(request):

    return render(request,"Atuendos/remera.html") 

def pantalon(request):

    return render(request,"Atuendos/pantalon.html") 

def inicio(request):
   
    return render(request,"Atuendos/inicio.html")    

def calzadoFormulario(request):

    if request.method == 'POST':

        mi_formulario = CalzadoFormulario(request.POST)

        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data

            marca = informacion['marca']
            talle = informacion['talle']

            mi_calzado = Calzado(marca = marca, talle = talle)
            mi_calzado.save()
     
        return render(request,"Atuendos/calzado.html")   
    
    else:
        
        mi_formulario = CalzadoFormulario()

    return render(request,"Atuendos/calzadoFormulario.html", {'miForm': mi_formulario})     

def busquedaCalzado(request):

    return render(request,'Atuendos/busquedaCalzado.html') 

def buscar(request):

    if request.GET("marca"):

        marca = request.GET("marca")
        calzados = Calzado.objects.filter(marca = marca)
        
        return render('Atuendos/resultadoBusqueda.html', {"marca":marca, "calzados":calzados})
    
    else:

        return HttpResponse('No enviaste el nombre de la marca')
from django.http import HttpResponse
from django.shortcuts import render
from .models import Calzado, Pantalon, Remera
# Create your views here.

def calzado(request,marca,talle):

    mi_calzado = Calzado(marca=marca, talle=talle)

    mi_calzado.save()


    return HttpResponse (f'El calzado es de la marca {mi_calzado.marca} con el talle {mi_calzado.talle}')

def remera(request,marca,talle,color):

    mi_remera = Remera(marca=marca,talle=talle,color=color)
    
    mi_remera.save()

    return HttpResponse(f'La remera es de la marca {mi_remera.marca}con el talle {mi_remera.talle} y del color {mi_remera.color}')

def pantalon(request,marca,talle,tipo_de_tela):

    mi_pantalon = Pantalon(marca=marca,talle=talle,tipo_de_tela=tipo_de_tela)
    
    mi_pantalon.save()
    
    return render(request,'C:/Users/mauro/Desktop/Proyecto nuevo/proyecto1/Atuendos/Templates/Atuendos/pantalon.html',{'marca':marca,'talle':talle,'tipo_de_tela':tipo_de_tela})

def inicio(request):
   
    return render(request,"Atuendos/inicio.html")    
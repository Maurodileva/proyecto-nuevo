from django.http import HttpResponse
from django.template import loader

def prueba(request):
    
    return HttpResponse ("Esta funcionando esta prueba")

def pruebaTemplate(request, nombre):

    plantilla = loader.get_template('templates1.html')
   
    return HttpResponse(plantilla.render({'name': nombre}))




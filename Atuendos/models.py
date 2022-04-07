from django.db import models

# Create your models here.

class Calzado(models.Model):

    marca = models.CharField('marca',max_length = 50)
    talle = models.IntegerField('talle')

class Remera(models.Model):

    marca= models.CharField('marca',max_length=50)
    talle= models.CharField('talle',max_length=3) 
    color= models.CharField('color',max_length=50)

class Pantalon(models.Model):

    marca= models.CharField('marca',max_length=50)
    talle = models.IntegerField('talle')
    tipo_de_tela = models.CharField('tela',max_length=50)

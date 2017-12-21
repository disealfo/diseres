# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=100,blank=True)
    descripcion = models.TextField(max_length=500)


class Direccion(models.Model):
    direccion = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

class Telefono(models.Model):
    numero = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)


class Persona(models.Model):
    usuario = models.OneToOneField(User)
    rol = models.ForeignKey(Rol, null= True , blank=True,on_delete=models.CASCADE)
    telefono = models.ForeignKey(Telefono, null= True, blank= True , on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion,null= True, blank= True , on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    correo = models.EmailField()

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.ForeignKey(Telefono, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)

class tipoEstablecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField()
    precio = models.DecimalField()
    descripcion = models.TextField(max_length=500)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField()
    unidades = models.IntegerField()


class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100, blank=True)


class Reserva(models.Model):
    fecha = models.DateField()
    establecimiento = models.ForeignKey(Establecimiento,null=True, blank=True, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,null=True, blank=True, on_delete=models.CASCADE)





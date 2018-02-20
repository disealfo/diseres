# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_establishment.models import Phone, Address
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=500)


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    PERSON_GENDER =(
        (MALE,'Masculino'),
        (FEMALE,'Femenino'),
        (OTHER,'Otro'),
    )
    user = models.OneToOneField(User)
    rol = models.ForeignKey(Rol, null= True , blank=True,on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, null= True, blank= True , on_delete=models.CASCADE)
    address = models.ForeignKey(Address,null= True, blank= True , on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=PERSON_GENDER,
        blank=True,
    )
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)
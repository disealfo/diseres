# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_products.models import Product
from app_services.models import Service
# Create your models here.
class Phone(models.Model):
    number = models.IntegerField()
    description = models.TextField(max_length=500, null=True, blank=True,)

class Address(models.Model):
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True,)


class EstablishmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.ForeignKey(Phone, null=True, blank=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
    establishmentType = models.ForeignKey(EstablishmentType, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True, blank=True, on_delete=models.CASCADE)
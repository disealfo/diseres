# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(max_length=500)

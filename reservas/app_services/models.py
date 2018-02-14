# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    price = models.IntegerField()
    description = models.TextField(max_length=500)

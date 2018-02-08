# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app_establishment.models import Establishment
from app_people.models import Person

class Reservation(models.Model):
    date = models.DateField()
    establishment = models.ForeignKey(Establishment,null=True, blank=True, on_delete=models.CASCADE)
    person = models.ForeignKey(Person,null=True, blank=True, on_delete=models.CASCADE)

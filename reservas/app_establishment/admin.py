# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Phone, Address, EstablishmentType, Establishment
from django.contrib import admin

# Register your models here.
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(EstablishmentType)
admin.site.register(Establishment)


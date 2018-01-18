# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin


from models import Persona
from models import Establecimiento
from models import Direccion
from models import Telefono
from models import Rol
from models import Reserva
from models import Producto
from models import Servicio
from models import TipoEstablecimiento


admin.site.register(Persona)
admin.site.register(Establecimiento)
admin.site.register(TipoEstablecimiento)
admin.site.register(Direccion)
admin.site.register(Telefono)
admin.site.register(Rol)
admin.site.register(Reserva)
admin.site.register(Producto)
admin.site.register(Servicio)
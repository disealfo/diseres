# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from models import Service
from forms import ServiceForm
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


#def my_view(request):
#	return render(request, 'services/form_service.html')

class ServiceList(ListView):
    model = Service
    template_name ='services/serviceList.html'


class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/serviceForm.html'
    success_url = reverse_lazy('services:listServices')
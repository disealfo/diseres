# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import serviceForm
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def my_view(request):
	return render(request, 'services/form_service.html')

def registerService(request):
	if request.method ==  "POST":
		form = serviceForm(request.POST)
		if form.is_valid():
			print "IS_VALID"

	else:
			form = serviceForm()
	return render(request,"services/form_service.html",{"formu":form})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.defaults import page_not_found


def error_404(request):

	return  render(request,  'errors/404.html')

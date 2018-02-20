# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from forms import PersonForm,UserForm,PhoneForm,AddresForm
from django.views.generic import ListView, CreateView
from models import Person

class PersonList(ListView):
    model = Person
    template_name = 'people/form_person.html'

class PersonCreate(CreateView):
    model = Person
    template_name = 'people/form_person.html'
    form_class = PersonForm
    second_form_class = UserForm
    third_form_class = PhoneForm
    fourth_form_class = AddresForm

    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        form4 = self.fourth_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            person = form.save(commit= False)
            person.user = form2.save()
            person.phone = form3.save()
            person.address = form4.save()
            person.save()
            return HttpResponseRedirect("index.html")
        else :
            return self.render_to_response(self.get_context_data(form = form, form2 = form2, form3 = form3, form4 = form4))



#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.shortcuts import render
from UNAG.apps.general.models import *

def lista_centros(request):
	centros = centro.objects.all()
	contexto = {'centros':centros}
	return render(request,'webservice/lista_centros.html', contexto)







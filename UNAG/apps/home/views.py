#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext #permite el envio de datos hacia la plantilla
from django.core.mail import EmailMultiAlternatives #enviamos HTML
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf.global_settings import PASSWORD_HASHERS as default_hashers
from django.contrib.auth.hashers import (is_password_usable, 
    check_password, make_password, PBKDF2PasswordHasher, 
    PBKDF2SHA1PasswordHasher, get_hasher)
from django.contrib.auth.decorators import permission_required, login_required
import csv
import xlrd
import xlwt

from UNAG.apps.home.forms import *
from UNAG.apps.general.models import *
from UNAG.apps.registro.models import *
from UNAG.apps.home.models import *

def view_index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def view_login(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('vista_main_first')) #redirecciona a la raiz
	else:
		if request.method=="POST":
			form = FormLogin(request.POST)
			if form.is_valid():
				print 'PASO POR AQUI 1'
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active: #si el usuario no es nullo y esta activo
					print 'PASO POR AQUI 2'
					login(request, usuario) #crea la sesion
					user = User.objects.get(id=request.user.id)
					if user.tipo_usuario.descripcion == 'Superusuario':
						return HttpResponseRedirect(reverse('vista_main_first')) #redirige a la raiz
					elif user.tipo_usuario.id == 3 or user.tipo_usuario.id == 12 or user.tipo_usuario.id == 13 or user.tipo_usuario.id == 5 or user.tipo_usuario.id == 14:
						return HttpResponseRedirect(reverse('vista_index_docente')) #redirige al censo de docentes
					elif user.tipo_usuario.descripcion == 'Alumno':
						print 'PASO POR AQUI 3'
						return HttpResponseRedirect(reverse('vista_index_alumno')) #redirige a la raiz
					else:
						mensaje = 'El usuario <<  '+user.username[:-4]+'****  >> no tiene los permisos necesarios para ingresar al modulo o no existe en el sistema.'
						logout(request)
				else:
					mensaje = "Usuario y/o Password incorrecto"	
		form = FormLogin()
		ctx={'form':form, 'mensaje':mensaje}			
		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

def view_logout(request):
	logout(request)
	return HttpResponseRedirect('/sare/')

def view_senso_logout(request):
	logout(request)
	return HttpResponseRedirect('/sare/')

@permission_required('home.can_view_menu', login_url='/logout/')
def view_main_first(request):
	return render_to_response('home/menu_principal2.html', context_instance=RequestContext(request))

def view_main_student(request):	
	return render_to_response('alumnos/alumnos_index.html', context_instance=RequestContext(request))

def view_main_teacher(request):
	return render_to_response('docentes/docentes_index.html', context_instance=RequestContext(request))

@permission_required('home.can_view_menu_registro', login_url='/logout/')
def view_main_administration(request):
	campuslen = 0; depto_academico = 0; carreraslen = 0; asociacionesCamplen = 0; centrosRegionaleslen = 0;

	campuslen = len(campus.objects.all())
	depto_academicoslen = len(departamento_academico.objects.all())
	carreraslen = len(carrera.objects.all())
	asociacionesCamplen = len(asoc_campesina.objects.all())
	centrosRegionaleslen = len(centro.objects.all())

	ctx = {'campuslen':campuslen, 'depto_academicoslen': depto_academicoslen, 
	'carreraslen': carreraslen, 'asociacionesCamplen': asociacionesCamplen,
	'centrosRegionaleslen':centrosRegionaleslen}
	
	return render_to_response('general/administracion_index.html', ctx, context_instance=RequestContext(request))

#vista inicio pagina de senso
@permission_required('home.can_view_home_censo', login_url='/logout/')
def view_home_senso(request):
	centros_list = []
	if centro.objects.all():
		print 'hay centros'
		centros_list = centro.objects.all()
	ctx = {'centro': centros_list}	
	return render_to_response('senso/inicio.html', ctx, context_instance=RequestContext(request))	



def view_excel(request):

	if request.method == 'POST':
	
		form = excelForm(request.POST, request.FILES)
		input_excel = request.FILES['archivo']
		book = xlrd.open_workbook(file_contents=input_excel.read())
		sh = book.sheet_by_index(0)

		row=0

		#crear hoja alumnos
		default_style = xlwt.Style.default_style
		datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
		date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
		book = xlwt.Workbook(encoding='utf8')
		sheet = book.add_sheet('alumnos')

		try:
			while sh.cell_value(rowx=row,colx=0) !='' :
				#print sh.cell_value(rowx=row,colx=0)
				random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
				random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
				num_cuenta=sh.cell_value(rowx=row,colx=0)+str(random_number_cuenta)
				objT=tipo_usuario.objects.get(id=4)
				#print objT
				grupo = Group.objects.get(id=2)
				#password=make_password(random_number, 'seasalt', 'pbkdf2_sha256')
				user = User.objects.create_user(num_cuenta, 'example@example.com', random_number)
				user.groups.add(grupo)
				user.tipo_usuario=objT
				user.codigo_registro=sh.cell_value(rowx=row,colx=1)
				user.save()
					
				val="Holasss World"
				sheet.write(row, 0, sh.cell_value(rowx=row,colx=0))
				sheet.write(row, 1, sh.cell_value(rowx=row,colx=1))
				sheet.write(row, 2, num_cuenta)
				sheet.write(row, 3, random_number)
				sheet.write(row, 4, objT.descripcion)
				row=row+1
				print row
			
			#print random_number
			#print make_password(random_number, 'seasalt', 'pbkdf2_sha256')

		except Exception, e:
			book.save("usuarios_alumnos.xls")
			#print ("error")

		ctx = {'formulario': form}

		#sh = book.sheet_by_index(0)

		return render_to_response('home/csv.html',ctx,context_instance=RequestContext(request))

	else:
		form = excelForm() 
		ctx = {'formulario': form}
		#print ('entro aqui')
		return render_to_response('home/csv.html',ctx,context_instance=RequestContext(request))

def view_excel_docente(request):

	if request.method == 'POST':
	
		form = excelForm(request.POST, request.FILES)
		input_excel = request.FILES['archivo']
		book = xlrd.open_workbook(file_contents=input_excel.read())
		sh = book.sheet_by_index(0)

		row=0

		#crear hoja docentes
		default_style = xlwt.Style.default_style
		datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
		date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
		book = xlwt.Workbook(encoding='utf8')
		sheet = book.add_sheet('docentes')

		try:
			while sh.cell_value(rowx=row,colx=0) !='' :
				#print sh.cell_value(rowx=row,colx=0)
				random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
				random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
				num_cuenta=sh.cell_value(rowx=row,colx=0)+str(random_number_cuenta)
				objT=tipo_usuario.objects.get(id=3)
				#print objT
				grupo = Group.objects.get(id=1)
				#password=make_password(random_number, 'seasalt', 'pbkdf2_sha256')
				user = User.objects.create_user(num_cuenta, 'example@example.com', random_number)
				user.groups.add(grupo)
				user.tipo_usuario=objT
				user.codigo_registro=sh.cell_value(rowx=row,colx=1)
				user.save()
					
				val="Holasss World"
				sheet.write(row, 0, sh.cell_value(rowx=row,colx=0))
				sheet.write(row, 1, sh.cell_value(rowx=row,colx=1))
				sheet.write(row, 2, num_cuenta)
				sheet.write(row, 3, random_number)
				sheet.write(row, 4, objT.descripcion)
				row=row+1
				print row
			
			#print random_number
			#print make_password(random_number, 'seasalt', 'pbkdf2_sha256')

		except Exception, e:
			book.save("usuarios_docentes.xls")
			#print ("error")

		ctx = {'formulario': form}

		#sh = book.sheet_by_index(0)

		return render_to_response('home/csv.html',ctx,context_instance=RequestContext(request))

	else:
		form = excelForm() 
		ctx = {'formulario': form}
		#print ('entro aqui')
		return render_to_response('home/csv.html',ctx,context_instance=RequestContext(request))

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext #permite el envio de datos hacia la plantilla
from django.core.mail import EmailMultiAlternatives #enviamos HTML
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, Permission
from django.conf.global_settings import PASSWORD_HASHERS as default_hashers
from django.contrib.auth.hashers import (is_password_usable, 
    check_password, make_password, PBKDF2PasswordHasher, load_hashers,
    PBKDF2SHA1PasswordHasher, get_hasher)
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required

from UNAG.apps.general.forms import *
from UNAG.apps.alumnos.forms import *
from UNAG.apps.registro.forms import *
from UNAG.apps.home.forms import *
from UNAG.apps.registro.models import *
from UNAG.apps.general.models import *
from UNAG.apps.home.models import *
def new_student_view(request):
	return render_to_response('alumnos/new_student.html', context_instance=RequestContext(request))

def profile_student_view(request):
	if request.method=='POST':
		formulario = AlumnoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/NuevoTipoDiseno')
	else:
		formulario = AlumnoForm()
	ctx = {'formulario': formulario}
	return render_to_response('alumnos/view_profile_student.html', ctx, context_instance=RequestContext(request))	

#vista administracion de personas alumnos para senso
#vista nuevo alumno PRIMER INGRESO
def view_add_people_alu(request):
	#si esta autenticado desloguearlo porque entonces no es un aspirante el que ingresa
	if request.user.is_authenticated():
		logout(request)

	anio=datetime.now().strftime("%Y")
	random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
	url_error = '/censo/primeringreso/add/'
	random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
	mensaje=''
	if request.method == 'POST':
		formulario = AspirantePersonaForm(request.POST, request.FILES)
		formulario_alu = AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid() and formulario_alu.is_valid():
			num_cuenta=formulario.cleaned_data['identidad']+str(random_number_cuenta)
			#crear un usuario inactivo para la persona
			user = User.objects.create_user(num_cuenta, formulario.cleaned_data['correo_electronico'], make_password(random_number, 'seasalt', 'pbkdf2_sha256'))
			#crear persona

			try:
				#crear persona
				person = formulario.save(commit = False)
				person.usuario=user
				person.usuario_creador=user
				person.fecha_creacion=datetime.now()
				person.usuario_modificador=user
				person.fecha_modificacion=datetime.now()
				person.save() #guardar persona	
				print 'se creo persona'

				#crear alumno
				form = formulario_alu.save(commit = False)
				form.persona=person
				form.usuario_creador = user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = user
				form.fecha_modificacion = datetime.now()
				form.save()
				print 'se creo alumno'

				# guardar many to many fields
				formulario.save_m2m() 
				formulario_alu.save_m2m()

				#actualizar datos de usuario
				objT=tipo_usuario.objects.get(id=10)
				grupo = Group.objects.get(id=2)
				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.is_staff=False
				user.is_active=False
				user.is_superuser=False
				user.groups.add(grupo)
				user.tipo_usuario=objT
				user.date_joined=datetime.now()
				user.save()

				print 'guardo titulos y centros y jornadas y usuario'

			except Exception, e:
				User.objects.filter(id=user.id).delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'error al crear alumno'
				return render_to_response('alumnos/censo_error.html', {'url': url_error}, context_instance=RequestContext(request))
			
			
			#else:
			#print 'error al crear persona'
			#print 'eliminando usuario'+str(user.id)
			#User.objects.filter(id=user.id).delete()
			return render_to_response('alumnos/censo_exito.html', {'nombre':person.nombre_completo} , context_instance=RequestContext(request))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = AspirantePersonaForm()
		formulario_alu = AlumnoForm()
	return render_to_response('general/new_persona.html', {'formulario':formulario, 'formulario_alu':formulario_alu, 'mensaje':mensaje}, context_instance=RequestContext(request))


#vista nuevo alumno REINGRESO
@permission_required('alumnos.add_alumnos', login_url='/censo/logout/')
def view_add_alumno_rein(request):
	mensaje=''
	url_error = '/censo/reingreso/add/'
	user = User.objects.get(id=request.user.id)
	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
		return HttpResponseRedirect(reverse('vista_index_alumno'))
	except persona.DoesNotExist:
		print 'no existe datos de persona'

	if request.method == 'POST':
		formulario = AlumnoPersonaForm(request.POST, request.FILES)
		formulario_alu = AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid() and formulario_alu.is_valid():
			#crear un objeto con el usuario logueado
			user = User.objects.get(id=request.user.id)

			try:
				#crear persona
				person = formulario.save(commit = False)
				person.usuario=request.user
				person.usuario_creador=request.user
				person.fecha_creacion=datetime.now()
				person.usuario_modificador=request.user
				person.fecha_modificacion=datetime.now()
				person.save() #guardar persona
						
				print 'se creo persona'

				#crear alumno
				form = formulario_alu.save(commit = False)
				form.persona=person
				form.codigo_registro= user.codigo_registro
				form.usuario_creador = request.user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				print 'se creo alumno'

				# guardar many to many fields
				formulario.save_m2m() 
				formulario_alu.save_m2m()
				print 'guardo titulos y centros y jornadas'

				#actualizar datos de usuario
				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.email=formulario.cleaned_data['correo_electronico']
				user.save()

			except Exception, e:
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'error al crear alumno'
				return render_to_response('alumnos/censo_error.html', {'url': url_error}, context_instance=RequestContext(request))

			return HttpResponseRedirect(reverse('vista_index_alumno'))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = AlumnoPersonaForm()
		formulario_alu = AlumnoForm()
	return render_to_response('general/new_persona_reingreso.html', {'formulario':formulario, 'formulario_alu':formulario_alu, 'mensaje':mensaje, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}, context_instance=RequestContext(request))

#vista editar informacion de persona en alumno de reingreso
@permission_required('alumnos.change_alumnos', login_url='/censo/logout/')
def view_persona_alumno_edit(request):
	try:
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.descripcion == 'Alumno':
			if request.method == 'POST':
				objPersona = persona.objects.get(usuario_id = request.user.id)
				formulario = AlumnoPersonaEditForm(request.POST, instance = objPersona)
				if formulario.is_valid():
					user = User.objects.get(id=request.user.id)
					form = formulario.save(commit = False)
					form.usuario_modificador = request.user
					form.fecha_modificacion = datetime.now()
					form.save()
					formulario.save_m2m()

					#actualizar datos de usuario
					user.first_name=formulario.cleaned_data['nombres']
					user.last_name=formulario.cleaned_data['apellidos']
					user.email=formulario.cleaned_data['correo_electronico']
					user.telefono=formulario.cleaned_data['celular']
					user.save()
					return HttpResponseRedirect(reverse('vista_index_alumno'))
				else:
					ctx = {'formulario': formulario, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}
					return render_to_response('alumnos/senso_persona_alumno_detalle.html', ctx, context_instance=RequestContext(request))
			else:
				print "editar-mostrar-data"
				
				if user.tipo_usuario.descripcion == 'Alumno':
					print user.tipo_usuario.descripcion + 'hoy si'
				objPersona = persona.objects.get(usuario_id = request.user.id)
				formulario = AlumnoPersonaEditForm(instance = objPersona)
				ctx = {'formulario': formulario,'identidad':request.user.username[:-4], 'registro':user.codigo_registro}
				return render_to_response('alumnos/senso_persona_alumno_detalle.html', ctx, context_instance=RequestContext(request))
	except Exception, e:
		print "Error al acceder a datos del usuario"
		return HttpResponseRedirect(reverse('vista_index_alumno'))

#vista para editar informacion del alumno de reingreso
@permission_required('alumnos.change_alumnos', login_url='/censo/logout/')
def view_senso_alumno_edit(request):
	try:
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.descripcion == 'Alumno':
			persona_id=persona.objects.get(usuario_id=request.user.id).id
			if request.method == 'POST':
				if alumnos.objects.filter(persona_id=persona_id): # si hay persona y hay alumno
					objAlumno = alumnos.objects.get(persona_id=persona_id)
					formulario = AlumnoForm(request.POST, instance = objAlumno)
					if formulario.is_valid():
						form = formulario.save(commit = False)
						form.codigo_registro=user.codigo_registro
						form.usuario_modificador = request.user
						form.fecha_modificacion = datetime.now()
						form.save()
						formulario.save_m2m()
						return HttpResponseRedirect(reverse('vista_index_alumno'))
					else:
						ctx = {'formulario': formulario}
						return render_to_response('alumnos/senso_alumno_detalle.html', ctx, context_instance=RequestContext(request))
				else: # si hay persona pero no alumno
					formulario = AlumnoForm(request.POST)
					if formulario.is_valid():
						form = formulario.save(commit = False)
						form.persona=persona.objects.get(usuario_id=request.user.id)
						form.codigo_registro=user.codigo_registro
						form.usuario_creador = request.user
						form.fecha_creacion = datetime.now()
						form.usuario_modificador = request.user
						form.fecha_modificacion = datetime.now()
						form.save()
						formulario.save_m2m()
						return HttpResponseRedirect(reverse('vista_index_alumno'))
					else:
						ctx = {'formulario': formulario}
						return render_to_response('alumnos/senso_alumno_detalle.html', ctx, context_instance=RequestContext(request))
			else:
				print "editar-mostrar-data"
				if alumnos.objects.filter(persona_id=persona_id): # si hay persona y hay alumno
					objAlumno = alumnos.objects.get(persona_id=persona_id)
					formulario = AlumnoForm(instance = objAlumno)
				else:
					formulario = AlumnoForm()
				ctx = {'formulario': formulario}
				return render_to_response('alumnos/senso_alumno_detalle.html', ctx, context_instance=RequestContext(request))
	except Exception, e:
		print "Error al acceder a datos del usuario"
		return HttpResponseRedirect(reverse('vista_index_alumno'))

def view_login_reingreso(request):
	mensaje=""
	if request.user.is_authenticated():
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.descripcion == 'Alumno':
			return HttpResponseRedirect(reverse('vista_index_alumno')) #redirecciona a la raiz
		else:
			logout(request)
			return HttpResponseRedirect(reverse('vista_login_reingreso')) #redirecciona al login
	else:
		if request.method=="POST":
			form = FormLogin(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active: #si el usuario no es nullo y esta activo
					login(request, usuario) #crea la sesion
					user = User.objects.get(id=request.user.id)
					if user.tipo_usuario.descripcion == 'Alumno':
						return HttpResponseRedirect(reverse('vista_index_alumno')) #redirige a la raiz
					else:
						return HttpResponseRedirect(reverse('vista_senso_logout'))
				else:
					mensaje = "Usuario y/o Password incorrecto"	
		form = FormLogin()
		ctx={'form':form, 'mensaje':mensaje}			
		return render_to_response('home/login_reingreso.html', ctx, context_instance=RequestContext(request))

@permission_required('alumnos.change_alumnos', login_url='/censo/logout/')
def view_index_alumno(request):
	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
	except persona.DoesNotExist:
		return HttpResponseRedirect(reverse('vista_nuevo_reingreso'))

	ctx=[]
	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
		print persona_id
		alumno=alumnos.objects.get(persona_id=persona_id)
		header="Estado:"
		msg_completar="Datos actualizados correctamente!"
		alerta="alert alert-success"
		ctx={'mensaje':msg_completar, 'alert': alerta, 'header': header}
		grupo = Group.objects.get(id=4)
	except Exception, e:
		header="Estado:"
		alerta="alert alert-warning"
		msg_completar="Aun no has ingresado toda tu informacion."
		ctx={'mensaje':msg_completar, 'alert': alerta, 'header': header}
	return render_to_response('alumnos/senso_index_alumno.html', ctx, context_instance=RequestContext(request))
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext #permite el envio de datos hacia la plantilla
from django.core.mail import EmailMultiAlternatives #enviamos HTML
from django.contrib.auth import login, logout, authenticate
from django.conf.global_settings import PASSWORD_HASHERS as default_hashers
from django.contrib.auth.hashers import (is_password_usable, 
    check_password, make_password, PBKDF2PasswordHasher, 
    PBKDF2SHA1PasswordHasher, get_hasher)
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Group

from UNAG.apps.general.forms import *
from UNAG.apps.alumnos.forms import *
from UNAG.apps.registro.forms import *
from UNAG.apps.home.forms import *
from UNAG.apps.registro.models import *
from UNAG.apps.general.models import *
from UNAG.apps.home.models import *

#Sarai
from django.shortcuts import render

#vistas de administracion departamentos Academicos------------------------------------------
@login_required
def view_administration_deptos_academics(request):
	deptos_academicos_list = []
	if departamento_academico.objects.all():
		deptos_academicos_list = departamento_academico.objects.all()
	ctx = {'departamentos_academicos': deptos_academicos_list}
	return render_to_response('registro/departamentos_academicos_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.add_departamento_academico', login_url='/administration/')
def view_depto_academic_add(request):
	if request.method=='POST':
		formulario = DepartamentoAcademicoForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.cod_usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.cod_usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/departamento_academico_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = DepartamentoAcademicoForm()
		ctx = {'formulario': formulario, 'ultimo': departamento_academico.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/departamento_academico_nuevo.html', ctx, context_instance=RequestContext(request))

def view_depto_academic_edit(request, idda=None):

		if request.method == 'POST':
			objDeptoA = departamento_academico.objects.get(pk = idda)
			formulario = DepartamentoAcademicoEditForm(request.POST, instance = objDeptoA)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.cod_usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_deptos_academics'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/departamento_academico_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objDeptoA = departamento_academico.objects.get(pk=idda)
			formulario = DepartamentoAcademicoEditForm(instance = objDeptoA)
			ctx = {'formulario': formulario, 'idda':idda}
			return render_to_response('registro/departamento_academico_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('registro.delete_departamento_academico', login_url='/administration/')
def view_delete_depto_academic(request,id_=None):

	if id_:
		departamento_academico.objects.filter(id=id_).delete()
		return HttpResponseRedirect(reverse('vista_administracion_deptos_academics'))


#vistas de administracion carreras----------------------------------------------------------
@login_required
def view_administration_carreras(request):
	carreras_list = []
	if carrera.objects.all():
		print 'hay carreras'
		carreras_list = carrera.objects.all()
	ctx = {'carrera': carreras_list}	
	return render_to_response('registro/carreras_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.add_carrera', login_url='/administration/')
def view_carrera_add(request):
	if request.method == 'POST':
		formulario = CarreraForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/carreras_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = CarreraForm()
		ctx = {'formulario': formulario, 'ultimo': carrera.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/carreras_nuevo.html', ctx, context_instance=RequestContext(request))		

def view_carrera_edit(request, id_=None):

		if request.method == 'POST':
			objCarrera = carrera.objects.get(pk = id_)
			formulario = CarreraForm(request.POST, instance = objCarrera)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_carreras'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/carreras_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objCarrera = carrera.objects.get(pk=id_)
			formulario = CarreraForm(instance = objCarrera)
			ctx = {'formulario': formulario, 'id':id_}
			return render_to_response('registro/carreras_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('registro.delete_carrera', login_url='/administration/')
def view_delete_carrera(request,id_=None):

	if id_:
		carrera.objects.filter(id=id_).delete()
		return HttpResponseRedirect(reverse('vista_administracion_carreras'))


#vistas de administracion documentos----------------------------------------------------------
@login_required
def view_administration_documentos(request):
	documentos_list = []
	if documentos.objects.all():
		print 'hay documentos'
		documentos_list = documentos.objects.all()
	ctx = {'documento': documentos_list}	
	return render_to_response('registro/documentos_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.add_documentos', login_url='/administration/')
def view_documento_add(request):
	if request.method == 'POST':
		formulario = DocumentoForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/documentos_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = DocumentoForm()
		ctx = {'formulario': formulario, 'ultimo': documentos.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/documentos_nuevo.html', ctx, context_instance=RequestContext(request))	

def view_documento_edit(request, id_=None):

		if request.method == 'POST':
			objDocumento = documentos.objects.get(pk = id_)
			formulario = DocumentoForm(request.POST, instance = objDocumento)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_documentos'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/documentos_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objDocumento = documentos.objects.get(pk=id_)
			formulario = DocumentoForm(instance = objDocumento)
			ctx = {'formulario': formulario, 'id':id_}
			return render_to_response('registro/documentos_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('registro.delete_documentos', login_url='/administration/')	
def view_delete_documento(request,id_=None):

	if id_:
		documentos.objects.filter(id=id_).delete()
		return HttpResponseRedirect(reverse('vista_administracion_documentos'))


#vistas de administracion asignaturas----------------------------------------------------------
@login_required
def view_administration_asignaturas(request):
	asignaturas_list = []
	if asignatura.objects.all():
		print 'hay asignaturas'
		asignaturas_list = asignatura.objects.all()
	ctx = {'asignatura': asignaturas_list}	
	return render_to_response('registro/asignaturas_index.html', ctx, context_instance=RequestContext(request))	


@permission_required('registro.add_asignatura', login_url='/administration/')
def view_asignatura_add(request):
	if request.method == 'POST':
		formulario = AsignaturaForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/asignaturas_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = AsignaturaForm()
		ctx = {'formulario': formulario, 'ultimo': asignatura.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/asignaturas_nuevo.html', ctx, context_instance=RequestContext(request))		


def view_asignatura_edit(request, id_=None):

		if request.method == 'POST':
			objAsignatura = asignatura.objects.get(pk = id_)
			formulario = AsignaturaForm(request.POST, instance = objAsignatura)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_asignaturas'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/asignaturas_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objAsignatura = asignatura.objects.get(pk=id_)
			formulario = AsignaturaForm(instance = objAsignatura)
			ctx = {'formulario': formulario, 'id':id_}
			return render_to_response('registro/asignaturas_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('registro.delete_asignatura', login_url='/administration/')
def view_delete_asignatura(request,id_=None):

	if id_:
		asignatura.objects.filter(id=id_).delete()
		return HttpResponseRedirect(reverse('vista_administracion_asignaturas'))


#vista administracion de personas docentes
@permission_required('registro.add_docente_departamento', login_url='/censo/logout/')
def view_add_people_docente(request):
	anio=datetime.now().strftime("%Y")
	random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
	url_error = '/censo/docente/add/'
	random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
	mensaje=''

	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
		return HttpResponseRedirect(reverse('vista_index_docente'))
	except persona.DoesNotExist:
		print 'no existe datos de persona'

	user = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		formulario = DocentePersonaForm(request.POST, request.FILES)
		formulario_doc = DocenteForm(request.POST, request.FILES)
		if formulario.is_valid() and formulario_doc.is_valid():
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
				
				#crear docente
				form = formulario_doc.save(commit = False)
				form.persona=person
				form.activo=True
				form.usuario_creador = request.user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				

				td=request.POST.get('tipo_docente')
				grupo=""				

				if td=='4':
					objT=tipo_usuario.objects.get(id=5)
					grupo = Group.objects.get(id=4)
					user.groups.add(grupo)
					user.tipo_usuario=objT
				elif td=='1':
					objT=tipo_usuario.objects.get(id=12)
					grupo = Group.objects.get(id=10)
					user.groups.add(grupo)
					user.tipo_usuario=objT
				elif td=='3':
					objT=tipo_usuario.objects.get(id=13)
					grupo = Group.objects.get(id=11)
					user.groups.add(grupo)
					user.tipo_usuario=objT

				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.email=formulario.cleaned_data['correo_electronico']
				user.save()

				form.save()
				print 'se creo docente'

				# guardar many to many fields
				formulario.save_m2m() 
				formulario_doc.save_m2m()
				print 'guardo titulos y centros y jornadas'

			except Exception, e:
				persona.objects.filter(pk=person.id).delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'se ha generado un error al guardar revise sus datos'
				return render_to_response('alumnos/censo_error.html', {'url': url_error}, context_instance=RequestContext(request))
						
			mensaje='Datos actualizados correctamente!'

			return HttpResponseRedirect(reverse('vista_index_docente'))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = DocentePersonaForm()
		formulario_doc = DocenteForm()
	return render_to_response('general/new_persona_docente.html', {'formulario':formulario, 'formulario_doc':formulario_doc, 'mensaje':mensaje, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}, context_instance=RequestContext(request))



#Vista //Sarai
def view_agregar_catedratico(request):	
	anio=datetime.now().strftime("%Y")
	random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
	url_error = 'catedratico/agregar/'
	random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
	mensaje=''
	user = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		formulario = CatedraticoPersonaForm(request.POST, request.FILES)
		formulario_doc = CatedraticoForm(request.POST, request.FILES)
		if formulario.is_valid() and formulario_doc.is_valid():
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
				
				#crear docente
				form = formulario_doc.save(commit = False)
				form.persona=person
				form.activo=True
				form.usuario_creador = request.user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				

				td=request.POST.get('tipo_docente')
				grupo=""				

				if td=='4':
					objT=tipo_usuario.objects.get(id=5)
					grupo = Group.objects.get(id=4)
					user.groups.add(grupo)
					user.tipo_usuario=objT
				elif td=='1':
					objT=tipo_usuario.objects.get(id=12)
					grupo = Group.objects.get(id=10)
					user.groups.add(grupo)
					user.tipo_usuario=objT
				elif td=='3':
					objT=tipo_usuario.objects.get(id=13)
					grupo = Group.objects.get(id=11)
					user.groups.add(grupo)
					user.tipo_usuario=objT

				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.email=formulario.cleaned_data['correo_electronico']
				user.save()

				form.save()
				print 'se creo docente'

				# guardar many to many fields
				formulario.save_m2m() 
				formulario_doc.save_m2m()
				print 'guardo titulos y centros y jornadas'

			except Exception, e:
				persona.objects.filter(pk=person.id).delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'se ha generado un error al guardar revise sus datos'
				return render_to_response('registro/senso_index_docente.html', {'url': url_error}, context_instance=RequestContext(request))
						
			mensaje='Datos actualizados correctamente!'

			return HttpResponseRedirect(reverse('vista_index_docente'))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = CatedraticoPersonaForm()
		formulario_doc = CatedraticoForm()
	return render_to_response('registro/nuevo_catedratico.html', {'formulario':formulario, 'formulario_doc':formulario_doc, 'mensaje':mensaje, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}, context_instance=RequestContext(request))
#fin



@permission_required('registro.change_docente_departamento', login_url='/censo/logout/')
def view_persona_docente_edit(request):
	try:
		user = User.objects.get(id=request.user.id)
		if request.method == 'POST':
			objPersona = persona.objects.get(usuario_id = request.user.id)
			formulario = DocentePersonaEditForm(request.POST, instance = objPersona)
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
				return HttpResponseRedirect(reverse('vista_index_docente'))
			else:
				ctx = {'formulario': formulario, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}
				return render_to_response('registro/senso_persona_docente_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objPersona = persona.objects.get(usuario_id = request.user.id)
			formulario = DocentePersonaEditForm(instance = objPersona)
			ctx = {'formulario': formulario, 'identidad':request.user.username[:-4], 'registro':user.codigo_registro}
			return render_to_response('registro/senso_persona_docente_detalle.html',  ctx, context_instance=RequestContext(request))
	except Exception, e:
		print "Error al acceder a datos del usuario"
		return HttpResponseRedirect(reverse('vista_index_docente'))

@permission_required('registro.change_docente_departamento', login_url='/censo/logout/')
def view_senso_docente_edit(request):
	try:
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.id == 3 or user.tipo_usuario.id == 12 or user.tipo_usuario.id == 13 or user.tipo_usuario.id == 5 or user.tipo_usuario.id == 14:
			persona_id=persona.objects.get(usuario_id=request.user.id).id
			if request.method == 'POST':
				if docente_departamento.objects.filter(persona_id=persona_id): #si hay persona y docente
					print "entro"
					objDocente = docente_departamento.objects.get(persona_id=persona_id)
					formulario = DocenteForm(request.POST, instance = objDocente)

					if formulario.is_valid():
						form = formulario.save(commit = False)
						form.persona=persona.objects.get(usuario_id=request.user.id)
						form.usuario_modificador = request.user
						form.fecha_modificacion = datetime.now()
						form.save()
						formulario.save_m2m()
						return HttpResponseRedirect(reverse('vista_index_docente'))
					else:
						ctx = {'formulario': formulario}
						return render_to_response('registro/senso_docente_departamento_detalle.html', ctx, context_instance=RequestContext(request))
				else: #si hay persona y pero no docente
					formulario = DocenteForm(request.POST)
					if formulario.is_valid():
						form = formulario.save(commit = False)
						form.persona=persona.objects.get(usuario_id=request.user.id)
						form.activo=True
						form.usuario_creador = request.user
						form.fecha_creacion = datetime.now()
						form.usuario_modificador = request.user
						form.fecha_modificacion = datetime.now()
						form.save()
						formulario.save_m2m()
						return HttpResponseRedirect(reverse('vista_index_docente'))
					else:
						ctx = {'formulario': formulario}
						return render_to_response('registro/senso_docente_departamento_detalle.html', ctx, context_instance=RequestContext(request))

			else:
				print "editar-mostrar-data"
				if docente_departamento.objects.filter(persona_id=persona_id):
					objDocente = docente_departamento.objects.get(persona_id=persona_id)
					formulario = DocenteForm(instance = objDocente)
				else:
					formulario = DocenteForm()
				ctx = {'formulario': formulario}
				return render_to_response('registro/senso_docente_departamento_detalle.html', ctx, context_instance=RequestContext(request))
	except Exception, e:
		print "Error al acceder a datos del usuario"
		return HttpResponseRedirect(reverse('vista_index_docente'))


def view_login_docente(request):
	mensaje=""
	if request.user.is_authenticated():
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.id == 3 or user.tipo_usuario.id == 12 or user.tipo_usuario.id == 13 or user.tipo_usuario.id == 5:
			return HttpResponseRedirect(reverse('vista_index_docente')) #redirecciona a la raiz
		else:
			logout(request)
			return HttpResponseRedirect(reverse('vista_login_docente')) #redirecciona al login
	else:
		if request.method=="POST":
			form = FormLogin(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active: #si el usuario no es nullo y esta activo
					login(request, usuario) #crea la sesion
					print "sesion creada"
					user = User.objects.get(id=request.user.id)
					print user.tipo_usuario.id
					if user.tipo_usuario.id == 3 or user.tipo_usuario.id == 12 or user.tipo_usuario.id == 13 or user.tipo_usuario.id == 5:
						return HttpResponseRedirect(reverse('vista_index_docente')) #redirige a la raiz
					else:
						return HttpResponseRedirect(reverse('vista_index_docente'))
				else:
					mensaje = "Usuario y/o Password incorrecto"	
		form = FormLogin()
		ctx={'form':form, 'mensaje':mensaje}			
		return render_to_response('home/login_docente.html', ctx, context_instance=RequestContext(request))

@permission_required('registro.change_docente_departamento', login_url='/censo/logout/')
def view_index_docente(request):
	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
	except persona.DoesNotExist:
		return HttpResponseRedirect(reverse('vista_nuevo_docente'))

	ctx=[]
	try:
		persona_id=persona.objects.get(usuario_id=request.user.id).id
		print persona_id
		docente=docente_departamento.objects.get(persona_id=persona_id)
		header="Estado:"
		msg_completar="Datos actualizados correctamente!"
		alerta="alert alert-success"
		ctx={'mensaje':msg_completar, 'alert': alerta, 'header': header}
	except Exception, e:
		header="Estado:"
		alerta="alert alert-warning"
		msg_completar="Aun no has ingresado toda tu informacion."
		ctx={'mensaje':msg_completar, 'alert': alerta, 'header': header}
	return render_to_response('registro/senso_index_docente.html', ctx, context_instance=RequestContext(request))

#vistas de administracion de Tipo de Asignatura
#by ciloe 18-09-2013
@login_required
def view_administration_type_subject(request):
	typesubject_list = []
	if tipo_asignatura.objects.all():
		print 'hay asignaturas'
		typesubject_list = tipo_asignatura.objects.all()
	ctx = {'tipo_A': typesubject_list}	
	return render_to_response('registro/tipo_asignatura_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.add_tipo_asignatura', login_url='/administration/')
def view_type_subject_add(request):
	if request.method == 'POST':
		formulario = TipoAsignaturaForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/tipo_asignaturas_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = TipoAsignaturaForm()
		ctx = {'formulario': formulario, 'ultimo': tipo_asignatura.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/tipo_asignaturas_nuevo.html', ctx, context_instance=RequestContext(request))	
			
def view_type_subject_edit(request, idta=None):

		if request.method == 'POST':
			objAsignatura = tipo_asignatura.objects.get(pk = idta)
			formulario = TipoAsignaturaForm(request.POST, instance = objAsignatura)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_tipo_asignaturas'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/tipo_asignatura_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objAsignatura = tipo_asignatura.objects.get(pk=idta)
			formulario = TipoAsignaturaForm(instance = objAsignatura)
			ctx = {'formulario': formulario, 'id':idta}
			return render_to_response('registro/tipo_asignatura_detalle.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.delete_tipo_asignatura', login_url='/administration/')
def view_type_subject_delete(request,idta=None):

	if idta:
		tipo_asignatura.objects.filter(id=idta).delete()
		return HttpResponseRedirect(reverse('vista_administracion_tipo_asignaturas'))

#vistas de tipos_condiciones_matricula
#by ciloe 19-09-2013

@login_required
def view_administration_enrollment_conditions(request):
	enrollment_list = []
	if tipos_condiciones_matricula.objects.all():
		print 'hay asignaturas'
		enrollment_list = tipos_condiciones_matricula.objects.all()
	ctx = {'tipoCM': enrollment_list}	
	return render_to_response('registro/tipos_condiciones_matricula_index.html', ctx, context_instance=RequestContext(request))	


@permission_required('registro.add_tipos_condiciones_matricula', login_url='/administration/')
def view__enrollment_conditions_add(request):
	if request.method == 'POST':
		formulario = TipoCMForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/tipos_condiciones_matricula_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = TipoCMForm()
		ctx = {'formulario': formulario, 'ultimo': tipos_condiciones_matricula.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/tipos_condiciones_matricula_nuevo.html', ctx, context_instance=RequestContext(request))	

def view_enrollment_conditions_edit(request, idtcm=None):

		if request.method == 'POST':
			objTCM = tipos_condiciones_matricula.objects.get(pk = idtcm)
			formulario = TipoCMForm(request.POST, instance = objTCM)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_tipo_cm'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/tipos_condiciones_matricula_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objTCM = tipos_condiciones_matricula.objects.get(pk=idtcm)
			formulario = TipoCMForm(instance = objTCM)
			ctx = {'formulario': formulario, 'id':idtcm}
			return render_to_response('registro/tipos_condiciones_matricula_detalle.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.delete_tipos_condiciones_matricula', login_url='/administration/')
def view_enrollment_conditions_delete(request,idtcm=None):

	if idtcm:
		tipos_condiciones_matricula.objects.filter(id=idtcm).delete()
		return HttpResponseRedirect(reverse('vista_administracion_tipo_cm'))


#administracion de Secciones

@login_required
def view_administration_secciones(request):
	secciones_list = []
	if seccion.objects.all():
		print 'hay secciones'
		secciones_list = seccion.objects.all()
	ctx = {'seccion': secciones_list}	
	return render_to_response('registro/seccion_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('registro.add_seccion', login_url='/administration/')
def view__secciones_add(request):
	if request.method == 'POST':
		formulario = SeccionForm(request.POST)		
		if formulario.is_valid():
			print "salvando"
			print formulario.cleaned_data['jornada']
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/seccion_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = SeccionForm()
		ctx = {'formulario': formulario, 'seccion':seccion.objects.all(), 'ultimo': seccion.objects.order_by('id').reverse()[:1]}
		return render_to_response('registro/seccion_nuevo.html', ctx, context_instance=RequestContext(request))	


def view_secciones_edit(request, idtcm=None):

		if request.method == 'POST':
			objTCM = seccion.objects.get(pk = idtcm)
			formulario = SeccionForm(request.POST, instance = objTCM)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_tipo_cm'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('registro/tipos_condiciones_matricula_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objTCM = seccion.objects.get(pk=idtcm)
			formulario = SeccionForm(instance = objTCM)
			ctx = {'formulario': formulario, 'id':idtcm}
			return render_to_response('registro/tipos_condiciones_matricula_detalle.html', ctx, context_instance=RequestContext(request))	

@login_required
def view_secciones_horario(request, idtcm=None):
	seccion_list = []
	if seccion.objects.filter(pk=idtcm):
			seccion_list = seccion.objects.filter(pk=idtcm)
	if request.method == 'POST':
		form_horario = HorarioHoraForm(request.POST)
		form_asignatura_seccion = AsignaturaSeccionForm(request.POST)		
		if form_horario.is_valid() and form_asignatura_seccion.is_valid():
			print "salvando"
			print formulario.cleaned_data['jornada']
			form = formulario.save(commit = False)
			form.usuario_creador = request.user
			form.fecha_creacion = datetime.now()
			form.usuario_modificador = request.user
			form.fecha_modificacion = datetime.now()
			form.save()
			return HttpResponseRedirect('')
		else:
			ctx = {'seccion': seccion_list, 'form_horario':form_horario, 'form_asignatura_seccion': form_asignatura_seccion}
			return render_to_response('registro/seccion_horario.html', ctx, context_instance=RequestContext(request)) 
	else:
		form_horario = HorarioHoraForm()
		form_asignatura_seccion = AsignaturaSeccionForm()
		ctx = {'seccion': seccion_list, 'id':idtcm, 'form_horario':form_horario, 'form_asignatura_seccion': form_asignatura_seccion}	
		return render_to_response('registro/seccion_horario.html', ctx, context_instance=RequestContext(request))	


@permission_required('registro.delete_seccion', login_url='/administration/')
def view_secciones_delete(request,idtcm=None):

	if idtcm:
		seccion.objects.filter(id=idtcm).delete()
		return HttpResponseRedirect(reverse('vista_administracion_secciones'))


#-----------------------------------------
#-----------------------------------------
#-----------------------------------------
#vista de formulario requisitos
#-----------------------------------------
#-----------------------------------------
#-----------------------------------------

@login_required
def view_administration_requirements(request):
	
	requirements_list = []
	if carrera.objects.all():
		requirements_list=carrera.objects.all()

	formulario = RequisitoForm()
	ctx = {'formulario':formulario ,'carreras': requirements_list}

	return render_to_response('registro/requisitos_index.html',ctx,context_instance=RequestContext(request))	


def view_requirements_ajax_list(request):
	if request.method == 'POST':

		html=''		
		html+='<table class="table table-striped table-bordered table-hover table-condensed" id="listar">'
		html+='<thead>'
		html+='<tr>'
		html+='<th>Código Registro</th>'
		html+='<th>Nombre Asignatura</th>'
		html+='<th>Observaciones</th>'
		html+='<th>Tipo Asignatura</th>'
		html+='<th>Requisitos</th>'
		html+='<th colspan="2">Acción</th>'							
		html+='</tr>'
		html+='</thead>'		
		html+='<tbody>'
						

		for a in asignatura.objects.filter(carrera_id=request.POST.get('id'), id__in=requisito.objects.values('asignatura_base').distinct()) :
			html+='<tr>'
			html+='<td>'+(a.codigo_registro).encode("utf-8")+'</td>'
			html+='<td>'
			cadena= (a.nombre_asignatura).encode("utf-8")
			html+=cadena
			html+='</td>'.encode("utf-8")
			html+='<td>'+(a.observaciones).encode("utf-8")+'</td>'
			html+='<td>'+str(a.tipo_asignatura) +'</td>'
			html+='<td>'

			for r in requisito.objects.filter(asignatura_base=a.id):
				html+=(r.asignatura_requisito.codigo_registro).encode("utf-8")
				html+='--'
				html+=(r.asignatura_requisito.nombre_asignatura).encode("utf-8")
				html+='<br/>'

			html+='</td>'

			html+="<td><center><a title='Ver' class='btn btn-success' onclick='redirigir("+str(a.pk)+");'><span class='glyphicon glyphicon-eye-open'></span></a></center></td>"
			html+='<td><center><a title="Borrar" class="btn btn-danger" onclick="confirmar('+str(a.pk)+');">'
			html+="<span class='glyphicon glyphicon-remove-circle'></span></a></center></td>"
			html+='</tr>'
			html+='</tbody>'
		html+='</table> '
		
		return HttpResponse(html)
	else:
		return HttpResponse(0)	


@permission_required('registro.add_requisitos', login_url='/administration/')
def view_requirements_add(request):
	if request.method == 'POST':
		formulario = RequisitoForm(request.POST)		
		if formulario.is_valid():
		
			for m in request.POST.getlist('modulos'):
				r=requisito.objects.create(
						asignatura_base=asignatura.objects.get(pk=request.POST.get('laboratorios')), 
						asignatura_requisito=asignatura.objects.get(pk=m), 
						usuario_creador=request.user, 
						fecha_creacion=datetime.now(), 
						usuario_modificador=request.user, 
						fecha_modificacion=datetime.now())
				r.save()	#guardar cada centro

			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/requisitos_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = RequisitoForm()
		ctx = {'formulario': formulario, 'labs': asignatura.objects.filter(tipo_asignatura_id=3).exclude(id__in=requisito.objects.filter(asignatura_requisito__tipo_asignatura=2).values_list('asignatura_base',flat=True)), 'modulos':asignatura.objects.filter(tipo_asignatura=2).exclude(id__in = requisito.objects.filter().values_list('asignatura_requisito', flat=True) )}
		return render_to_response('registro/requisitos_nuevo.html', ctx, context_instance=RequestContext(request))	



#by ciloe 5-Octubre-2013
def view_requirements_ajax_uv(request):
	if request.method == 'POST':	
		for c in asignatura.objects.filter(id=request.POST.get('id')):
			html='<label> Univades Valorativas:' + str(c.uv)+'</label> <input type="hidden" id="vuv" value="'+str(c.uv)+'"/>'
		return HttpResponse(html)
	else:
		return HttpResponse(0)	


def view_requirements_add_subjects(request):
	if request.method == 'POST':
		formulario = RequisitoForm(request.POST)		
		if formulario.is_valid():
		
			for m in request.POST.getlist('modulos'):
				r=requisito.objects.create(
						asignatura_base=asignatura.objects.get(pk=request.POST.get('asignatura')), 
						asignatura_requisito=asignatura.objects.get(pk=m), 
						usuario_creador=request.user, 
						fecha_creacion=datetime.now(), 
						usuario_modificador=request.user, 
						fecha_modificacion=datetime.now())
				r.save()

			return HttpResponseRedirect('')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('registro/requisitos_nuevo_al.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = RequisitoForm()
		ctx = {'formulario': formulario, 'asigna': asignatura.objects.filter(tipo_asignatura__in=(5,3)).exclude(id__in =requisito.objects.filter(asignatura_base__tipo_asignatura=5).values_list('asignatura_base',flat=True)).exclude(id__in =requisito.objects.filter(asignatura_requisito__tipo_asignatura=5, asignatura_base__tipo_asignatura=3).values_list('asignatura_base',flat=True)) }
		
		return render_to_response('registro/requisitos_nuevo_al.html', ctx, context_instance=RequestContext(request))	


def view_requirements_ajax_uv_subjects(request):
	if request.method == 'POST':

		for c in asignatura.objects.filter(id=request.POST.get('id')):
			html=""
			html+=' <label> Univades Valorativas:' + str(c.uv)+'</label> <input type="hidden" id="vuv" value="'+str(c.uv)+'"/>'
			html+='	<br/><br/>'
			html+='	<div id="selectores">'
			html+=' <label>Seleccione: &nbsp;</label>'
			html+=' <select id="id_modulos" name="modulos" multiple="multiple">'	
					
			for a in asignatura.objects.filter(tipo_asignatura__in=(5,3), carrera__in=asignatura.objects.filter(id=request.POST.get('id')).values_list('carrera')).exclude(id=request.POST.get('id')):
				html+='<option value="'+ str(a.id) +'">'+ a.nombre_asignatura +' </option>'
			html+='</select></div>'

		return HttpResponse(html)
	else:
		return HttpResponse(0)


def view_requirements_delete(request,idtcm=None):

	if idtcm:
		print('Entro A borrar requisito')
		requisito.objects.filter(asignatura_base=idtcm).delete()
		return HttpResponseRedirect(reverse('vista_administracion_requisito'))			

#by ciloe 17-Octubre-2013

def view_requirements_edit(request,idtcm=None):

			objrequisitos = asignatura.objects.filter(id__in = requisito.objects.filter(asignatura_base=idtcm).values_list('asignatura_requisito'))
			objAsigBase= asignatura.objects.get(id=idtcm)
			objAsigRe=asignatura.objects.filter(tipo_asignatura__in=(5,3)).exclude(id__in =requisito.objects.filter(asignatura_base=idtcm).values_list('asignatura_requisito')).exclude(id=idtcm)
			formulario=RequisitoForm()
			ctx = {'formulario': formulario,'requisitos':objrequisitos,'asigbase': objAsigBase, 'asigReq': objAsigRe }
			return render_to_response('registro/requisitos_detalle.html', ctx, context_instance=RequestContext(request))


#by ciloe 22 de octubre-2013 // Horrible esto
def view_requirements_ajax_update(request):
		if request.method == 'POST':
			requisito.objects.filter(asignatura_base=request.POST.get('id')).delete()
			
			for m in request.POST.getlist('id_requisitos'):
				r=requisito.objects.create(
						asignatura_base=asignatura.objects.get(pk=request.POST.get('id')), 
						asignatura_requisito=asignatura.objects.get(pk=m), 
						usuario_creador=request.user, 
						fecha_creacion=datetime.now(), 
						usuario_modificador=request.user, 
						fecha_modificacion=datetime.now())
				r.save()

			
			return HttpResponse(0)
	

#views administrar censo
@permission_required('home.can_view_menu_censo', login_url='/main_first/')
def view_administration_censo(request):
	secciones_list = []
	if seccion.objects.all():
		print 'hay secciones'
		secciones_list = seccion.objects.all()
	ctx = {'seccion': secciones_list}	
	return render_to_response('general/menu_censo_administracion.html', ctx, context_instance=RequestContext(request))	

@permission_required('home.can_view_avance_censo', login_url='/administration/censo/')
def view_avance_censo(request):
	alumnos_censados = alumnos.objects.filter(persona__tipo_persona__descripcion__iexact='estudiante reingreso').count()
	alumnos_no_censados = User.objects.filter(tipo_usuario__descripcion__iexact='alumno').count() - alumnos_censados - 1
	docentes_censados = docente_departamento.objects.filter(persona__tipo_persona__descripcion__iexact='docente').count()
	docentes_no_censados = User.objects.filter(tipo_usuario__in=[3,12,13,5]).count() - docentes_censados - 1
	ctx = {'alumnos_censados': alumnos_censados, 'alumnos_no_censados': alumnos_no_censados, 'docentes_censados': docentes_censados, 'docentes_no_censados': docentes_no_censados}	
	return render_to_response('registro/avance_censo.html', ctx, context_instance=RequestContext(request))	

@permission_required('home.can_recuperar_clave', login_url='/administration/censo/')
def view_recuperar_clave(request):
	if request.method == 'POST':
		identidad = request.POST.get('identidad')
		registro = request.POST.get('registro')
		
		if User.objects.filter(username__istartswith=identidad, codigo_registro=registro).count() == 1:
			user = User.objects.get(username__istartswith=identidad, codigo_registro=registro)
			random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
			random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
			usuario = identidad + str(random_number_cuenta)
			clave= make_password(random_number, 'seasalt', 'pbkdf2_sha256')

			#guardar usuario
			user.username = usuario
			user.password = clave
			user.save()
			mensaje="Clave Recuperada!"
			alerta="alert alert-success"
			ctx = {'mensaje': mensaje, 'alerta':alerta, 'username': usuario, 'password': random_number, 'tipo':user.tipo_usuario}
			return render_to_response('general/recuperar_clave.html', ctx, context_instance=RequestContext(request))	
		else:
			mensaje="No se pudo recuperar la clave!"
			alerta="alert alert-danger"
			ctx = {'mensaje': mensaje, 'alerta':alerta}
			return render_to_response('general/recuperar_clave.html', ctx, context_instance=RequestContext(request))	
		print clave
		print usuario
		print registro
		
	ctx = {'seccion': "hola"}	
	return render_to_response('general/recuperar_clave.html', ctx, context_instance=RequestContext(request))	

#Sarai
def menu_principal(request):
	return render(request,'registro/menu_principal_catedratico.html')
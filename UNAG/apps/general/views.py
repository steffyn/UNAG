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
from UNAG.apps.general.models import *
from UNAG.apps.registro.models import *
from UNAG.apps.home.models import *
import json


#vistas de administracion campus ---------------------------------------------------------
@login_required
def view_administration_campus(request):
	campus_list = []
	if Campus.objects.all():
		campus_list = Campus.objects.all()
	ctx = {'campus': campus_list}
	return render_to_response('general/campus_index.html', ctx,context_instance=RequestContext(request))

@permission_required('general.add_campus', login_url='/administration/')
def view_campus_add(request):
	if request.method=='POST':
		formulario = CampusForm(request.POST)		
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
			return render_to_response('general/campus_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = CampusForm()
		ctx = {'formulario': formulario, 'ultimo': Campus.objects.order_by('id').reverse()[:1]}
		return render_to_response('general/campus_nuevo.html', ctx, context_instance=RequestContext(request))

def view_campus_edit(request, idcampus=None):

		if request.method == 'POST':
			objCampus = Campus.objects.get(pk = idcampus)
			formulario = CampusForm(request.POST, instance = objCampus)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_campus'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('general/campus_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objCampus = Campus.objects.get(pk=idcampus)
			formulario = CampusEditForm(instance = objCampus)
			ctx = {'formulario': formulario, 'idcampus':idcampus}
			return render_to_response('general/campus_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('general.delete_campus', login_url='/administration/')
def view_delete_campus(request,idcampus=None):

	if idcampus:
		Campus.objects.filter(id=idcampus).delete()
		return HttpResponseRedirect(reverse('vista_administracion_campus'))


#vistas de administracion asociacion campesina----------------------------------------------
def view_administration_peasant_asociation(request):
	return render_to_response('general/asociaciones_campesinas_index.html', context_instance=RequestContext(request))	


#vistas de administracion centros regionales------------------------------------------------
def view_administration_regional_centers(request):
	return render_to_response('general/centros_regionales_index.html', context_instance=RequestContext(request))	


#vistas de administracion zonas--------------------------------------------------------------
def view_administration_zones(request):
	return render_to_response('general/zonas_index.html', context_instance=RequestContext(request))	


#vistas de administracion documentos---------------------------------------------------------
def view_administration_documents(request):
	return render_to_response('general/documentos_index.html', context_instance=RequestContext(request))	


#vistas de administracion jornadas laborales-------------------------------------------------
def view_administration_workdays(request):
	return render_to_response('general/jornadas_laborales_index.html', context_instance=RequestContext(request))		


#vistas de administracion usuarios-----------------------------------------------------------
def view_administration_users(request):
	return render_to_response('general/usuarios_index.html', context_instance=RequestContext(request))			


#vistas de administracion estudiantes--------------------------------------------------------
def view_administration_students(request):
	return render_to_response('general/admin_alumnos_index.html', context_instance=RequestContext(request))			


#vistas de administracion profesores---------------------------------------------------------
def view_administration_teachers(request):
	return render_to_response('general/admin_docentes_index.html', context_instance=RequestContext(request))			


#vista de administracion de edificios--------------------------------------------------------
def view_administration_buildings(request):
	return render_to_response('general/edificios_index.html', context_instance=RequestContext(request))			


#vista de administracion de dormitorios------------------------------------------------------
def view_administration_bedroom(request):
	return render_to_response('general/dormitorios_index.html', context_instance=RequestContext(request))			


#vista de administracion de edificios--------------------------------------------------------
#by ciloe 5-09-2013-----
@login_required
def view_administration_buildings(request):
	print  "Entro aqui :("
	edif_list = []
	if Edificios.objects.all():
		edif_list = Edificios.objects.all()
	ctx = {'edificios': edif_list}

	return render_to_response('general/edificios_index.html',ctx, context_instance=RequestContext(request))			

@permission_required('general.add_edificios', login_url='/administration/')
def view_buildings_add(request,idde=None):
	
		if request.method == 'POST':
			print "salvando1"
			formulario = EdificiosForm(request.POST)		
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
				return render_to_response('general/edificios_nuevo.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = EdificiosForm()
			ctx = {'formulario': formulario, 'ultimo': Edificios.objects.order_by('id').reverse()[:1]}
			return render_to_response('general/edificios_nuevo.html', ctx, context_instance=RequestContext(request))

def view_buildings_edit(request,idde=None):

			if request.method == 'POST':
				objedif = Edificios.objects.get(pk = idde)
				formulario = EdificiosForm(request.POST, instance = objedif)
				if formulario.is_valid():
					form = formulario.save(commit = False)
					form.usuario_modificador = request.user
					form.fecha_modificacion = datetime.now()
					form.save()
					return HttpResponseRedirect(reverse('vista_administracion_edificios'))
				else:
					ctx = {'formulario': formulario}
					return render_to_response('general/edificios_detalle.html', ctx, context_instance=RequestContext(request))
			else:
				print "editar-mostrar-data"
				objedif = Edificios.objects.get(pk=idde)
				formulario = EdificiosForm(instance=objedif)
				ctx = {'formulario': formulario, 'idedificio':idde}
			return render_to_response('general/edificios_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('general.delete_edificios', login_url='/administration/')
def view_delete_buildings(request,idde=None):

	if idde:
		Edificios.objects.filter(id=idde).delete()
		return HttpResponseRedirect(reverse('vista_administracion_edificios'))


# vista para recargar por ajax los municipios de un depto en model persona
def view_people_ajax_municipio(request):
	if request.method == 'POST':
		html=""
		html+='<label for="id_'+request.POST.get('name')+'">'+request.POST.get('name')[:1].upper()+request.POST.get('name')[1:]+'&nbsp; </label>'
		html+='<select id="id_'+request.POST.get('name')+'" class="chosen-select" name="'+request.POST.get('name')+'" required="required">'
		html+='<option value selected="selected">---------</option>'
		if request.POST.get('bandera') == 'd':
			for c in Municipio.objects.filter(departamento=request.POST.get('id')):
				cod = c.id
				cod_mun = '' + c.codigo_municipio + ' | '
				name = c.descripcion
				html+='<option value='+str(cod)+'>'+cod_mun+name+'</option>' 
		elif request.POST.get('bandera') == 'm':
			for c in Aldea.objects.filter(municipio=request.POST.get('id')):
				cod = c.id
				name = c.descripcion
				html+='<option value='+str(cod)+'>'+name+'</option>' 
		elif request.POST.get('bandera') == 'a':
			for c in Caserio.objects.filter(aldea=request.POST.get('id')):
				cod = c.id
				name = c.descripcion
				html+='<option value='+str(cod)+'>'+name+'</option>'
		elif request.POST.get('bandera') == 'c':
			for c in Barrio.objects.filter(caserio=request.POST.get('id')):
				cod = c.id
				name = c.descripcion
				html+='<option value='+str(cod)+'>'+name+'</option>'

		html+='</select>'
		return HttpResponse(html)
	else:
		return HttpResponse(0)


#vistas de administracion centros----------------------------------------------------------
@login_required
def view_administration_centros(request):
	centros_list = []
	if Centro.objects.all():
		print 'hay centros'
		centros_list = Centro.objects.all()
	ctx = {'centro': centros_list}	
	return render_to_response('general/centros_index.html', ctx, context_instance=RequestContext(request))	

@permission_required('general.add_centro', login_url='/administration/')
def view_centro_add(request):

	if request.method == 'POST':
		formulario = CentroForm(request.POST)		
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
			return render_to_response('general/centros_nuevo.html', ctx, context_instance=RequestContext(request)) 
	else:
		formulario = CentroForm()
		ctx = {'formulario': formulario, 'ultimo': Centro.objects.order_by('id').reverse()[:1]}
		return render_to_response('general/centros_nuevo.html', ctx, context_instance=RequestContext(request))		

def view_centro_edit(request, id_=None):

		if request.method == 'POST':
			objCentro = Centro.objects.get(pk = id_)
			formulario = CentroForm(request.POST, instance = objCentro)
			if formulario.is_valid():
				form = formulario.save(commit = False)
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect(reverse('vista_administracion_centros'))
			else:
				ctx = {'formulario': formulario}
				return render_to_response('general/centros_detalle.html', ctx, context_instance=RequestContext(request))
		else:
			print "editar-mostrar-data"
			objCentro = Centro.objects.get(pk=id_)
			formulario = CentroForm(instance = objCentro)
			ctx = {'formulario': formulario, 'id':id_}
			return render_to_response('general/centros_detalle.html', ctx, context_instance=RequestContext(request))

@permission_required('general.delete_centro', login_url='/administration/')
def view_delete_centro(request,id_=None):

	if id_:
		Centro.objects.filter(id=id_).delete()
		return HttpResponseRedirect(reverse('vista_administracion_centros'))


#vista de administracion de dormitorios------------------------------------------------------
#by ciloe 17-09-2013 
@login_required
def view_administration_bedroom(request):
	bedroom_list = []
	if  EstructuraEdificio.objects.all():
		bedroom_list =  EstructuraEdificio.objects.all()
	ctx = {'dormitorios': bedroom_list}

	return render_to_response('general/dormitorios_index.html', ctx, context_instance=RequestContext(request))			



@permission_required('general.add_dormitorio', login_url='/administration/')
def view_bedroom_add(request):
	
		if request.method == 'POST':
			
			formulario = DormitorioForm(request.POST)		
			if formulario.is_valid():
				
				form = formulario.save(commit = False)
				form.usuario_creador = request.user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = request.user
				form.fecha_modificacion = datetime.now()
				form.save()
				return HttpResponseRedirect('')
			else:
				ctx = {'formulario':formulario}
				return render_to_response('general/dormitorios_nuevo.html', ctx, context_instance=RequestContext(request)) 
		
		else:
			formulario = DormitorioForm()
			ctx = {'formulario': formulario, 'ultimo':  EstructuraEdificio.objects.order_by('id').reverse()[:1]}
			return render_to_response('general/dormitorios_nuevo.html', ctx, context_instance=RequestContext(request))


#by ciloe 09-10-2013
def view_bedroom_ajax(request):
	if request.method == 'POST':	
		data= Edificios.objects.filter(id=request.POST.get('id')).values_list('tipo_edificio',flat=True)
		print 'lakjsdlkajsdlasd---->', json.dumps('{"tipo":'+str(data)+'}')
		return HttpResponse(json.dumps('{"tipo":'+str(data)+'}'), content_type='application/json')
	else:
		return HttpResponse(0)	


def view_bedroom_edit(request,iddo=None):

			if request.method == 'POST':
				objdorm =  EstructuraEdificio.objects.get(pk = iddo)
				formulario = DormitorioForm(request.POST, instance = objdorm)
				if formulario.is_valid():
					form = formulario.save(commit = False)
					form.usuario_modificador = request.user
					form.fecha_modificacion = datetime.now()
					form.save()
					return HttpResponseRedirect(reverse('vista_administracion_dormitorios'))
				else:
					ctx = {'formulario': formulario}
					return render_to_response('general/dormitorios_detalle.html', ctx, context_instance=RequestContext(request))
			else:
				print "editar-mostrar-data"
				objdorm =  EstructuraEdificio.objects.get(pk=iddo)
				formulario = DormitorioForm(instance=objdorm)
				ctx = {'formulario': formulario, 'iddo':iddo}
			return render_to_response('general/dormitorios_detalle.html', ctx, context_instance=RequestContext(request))


@permission_required('general.delete_dormitorio', login_url='/administration/')
def view_bedroom_delete(request,iddo=None):

	if iddo:
		EstructuraEdificio.objects.filter(id=iddo).delete()
		return HttpResponseRedirect(reverse('vista_administracion_dormitorios'))

   

#vista de administracion de recursos humanos------------------------------------------------------
@login_required
def view_administration_recursohumano(request):
	return render_to_response('general/recursohumano_index.html', context_instance=RequestContext(request))			

#vista nuevo persona recurso humano
@permission_required('general.add_persona', login_url='/censo/logout/')
def view_add_recursohumano_normal(request):
	#si esta autenticado desloguearlo porque entonces no es un aspirante el que ingresa
	print "hola"
	anio=datetime.now().strftime("%Y")
	random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
	url_error = '/administration/people/add/recursohumano/normal'
	random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
	mensaje=''
	if request.method == 'POST':
		formulario = PersonaForm(request.POST, request.FILES)
		print request.POST.get('tipo_persona')
		if formulario.is_valid():
			num_cuenta=formulario.cleaned_data['identidad']+str(random_number_cuenta)
			#crear un usuario inactivo para la persona
			user = User.objects.create_user(num_cuenta, formulario.cleaned_data['correo_electronico'], random_number)
			#crear persona

			try:
				#crear persona
				person = formulario.save(commit = False)
				person.usuario=user
				person.usuario_creador=request.user
				person.fecha_creacion=datetime.now()
				person.usuario_modificador=request.user
				person.fecha_modificacion=datetime.now()
				 
				print 'se creo persona'

				#actualizar datos de usuario
				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.is_staff=False
				user.is_active=True
				user.is_superuser=False
				user.date_joined=datetime.now()
				#user.save()

				print 'guardo titulos y centros y jornadas y usuario'

				tp=request.POST.get('tipo_persona')
				grupo=""				

				if tp=='1' or tp=='2':
					objT=TipoUsuario.objects.get(id=4)
					grupo = Group.objects.get(id=2)
				elif tp=='5' or tp=='6' or tp=='7':
					objT=TipoUsuario.objects.get(id=5)
					grupo = Group.objects.get(id=4)
				elif tp=='11':
					objT=TipoUsuario.objects.get(id=6)
					grupo = Group.objects.get(id=5)
				elif tp=='10':
					objT=TipoUsuario.objects.get(id=7)
					grupo = Group.objects.get(id=6)
				elif tp=='13':
					objT=TipoUsuario.objects.get(id=8)
					grupo = Group.objects.get(id=7)
				elif tp=='14':
					objT=TipoUsuario.objects.get(id=9)
					grupo = Group.objects.get(id=8)
				elif tp=='1':
					objT=TipoUsuario.objects.get(id=10)
					grupo = Group.objects.get(id=2)
				elif tp=='3':
					objT=TipoUsuario.objects.get(id=3)
					grupo = Group.objects.get(id=1)
				elif tp=='9':
					objT=TipoUsuario.objects.get(id=12)
					grupo = Group.objects.get(id=10)
				else:
					objT=TipoUsuario.objects.get(id=13)
					grupo = Group.objects.get(id=11)


				person.save() #guardar persona	

				# guardar many to many fields
				formulario.save_m2m()

				user.groups.add(grupo)
				user.tipo_usuario=objT
				user.save()

			except Exception, e:
				User.objects.filter(id=user.id).delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'error al crear persona'
				return render_to_response('general/error.html', {'url': url_error}, context_instance=RequestContext(request))
				
			
			#else:
			#print 'error al crear persona'
			#print 'eliminando usuario'+str(user.id)
			#User.objects.filter(id=user.id).delete()
			return render_to_response('general/exito.html', {'nombre':person.nombre_completo, 'usuario': num_cuenta, 'password': random_number} , context_instance=RequestContext(request))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = PersonaForm()
	return render_to_response('general/new_persona_recursohumano.html', {'formulario':formulario, 'mensaje':mensaje}, context_instance=RequestContext(request))


#vista nuevo persona recurso humano docente
@permission_required('general.add_persona', login_url='/censo/logout/')
def view_add_recursohumano_docente(request):
	#si esta autenticado desloguearlo porque entonces no es un aspirante el que ingresa
	print "hola"
	anio=datetime.now().strftime("%Y")
	random_number_cuenta = User.objects.make_random_password(length=4, allowed_chars='0123456789')
	url_error = '/administration/people/add/recursohumano/docente'
	random_number = User.objects.make_random_password(length=8, allowed_chars='0123456789%!#qwertyuiopasdfghjklzxcvbnm')
	mensaje=''
	if request.method == 'POST':
		formulario = DocenteAdministrativoForm(request.POST, request.FILES)
		formulario_doc = DocenteForm(request.POST, request.FILES)
		print request.POST.get('tipo_docente')
		if formulario.is_valid() and formulario_doc.is_valid():
			num_cuenta=formulario.cleaned_data['identidad']+str(random_number_cuenta)
			#crear un usuario inactivo para la persona
			#user = User.objects.create_user(num_cuenta, formulario.cleaned_data['correo_electronico'], random_number)
			#crear persona
			identidad=formulario.cleaned_data['identidad']
			try:
				if User.objects.filter(username__istartswith=identidad).count() == 1:
					user = User.objects.get(username__istartswith=identidad)
					#crear persona
					person = formulario.save(commit = False)
					person.usuario=user
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

					#asignar grupo segun tipo de docente
					td=request.POST.get('tipo_docente')
					grupo=""				

					if td=='4':
						objT=TipoUsuario.objects.get(id=14)
						grupo = Group.objects.get(id=4)
						user.groups.add(grupo)
						user.tipo_usuario=objT
					elif td=='2':
						objT=TipoUsuario.objects.get(id=3)
						grupo = Group.objects.get(id=1)
						user.groups.add(grupo)
						user.tipo_usuario=objT
					elif td=='1':
						objT=TipoUsuario.objects.get(id=12)
						grupo = Group.objects.get(id=10)
						user.groups.add(grupo)
						user.tipo_usuario=objT
					elif td=='3':
						objT=TipoUsuario.objects.get(id=13)
						grupo = Group.objects.get(id=11)
						user.groups.add(grupo)
						user.tipo_usuario=objT

					#actualizar datos de usuario
					user.first_name=formulario.cleaned_data['nombres']
					user.last_name=formulario.cleaned_data['apellidos']
					user.is_staff=False
					user.is_active=True
					user.is_superuser=False
					user.date_joined=datetime.now()
					user.email=formulario.cleaned_data['correo_electronico']

					form.save()
					print 'se creo docente'

					# guardar many to many fields
					formulario.save_m2m() 
					formulario_doc.save_m2m()
					print 'guardo titulos y centros y jornadas'

					user.save()
				else:
					mensaje='No se encontró un usuario con esa identidad'
					print 'error al crear persona'
					return render_to_response('general/error.html', {'url': url_error}, context_instance=RequestContext(request))

			except Exception, e:
				User.objects.filter(id=user.id).delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				print 'error al crear persona'
				return render_to_response('general/error.html', {'url': url_error}, context_instance=RequestContext(request))
				
			
			#else:
			#print 'error al crear persona'
			#print 'eliminando usuario'+str(user.id)
			#User.objects.filter(id=user.id).delete()
			return render_to_response('general/exito.html', {'url': url_error, 'nombre':person.nombre_completo, 'usuario': user.username, 'password': "*******"} , context_instance=RequestContext(request))
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = DocenteAdministrativoForm()
		formulario_doc = DocenteForm()
	return render_to_response('general/new_persona_recursohumano_docente.html', {'formulario':formulario, 'formulario_doc': formulario_doc, 'mensaje':mensaje}, context_instance=RequestContext(request))



#vista vericar si la identidad existe y retornar el numero de registro
@permission_required('general.add_persona', login_url='/censo/logout/')
def view_recuperar_registro(request):
	if request.method == 'POST':
		identidad = request.POST.get('identidad')
		print identidad
		if User.objects.filter(username__istartswith=identidad).count() == 1 and len(identidad)==13:
			if Persona.objects.filter(identidad__istartswith=identidad).count() == 1:
				return HttpResponse("Ya existe una persona con esta Identidad")
			user = User.objects.get(username__istartswith=identidad)
			return HttpResponse(user.codigo_registro)
		else:
			return HttpResponse("No se ha podido encontrar el número de registro")
	else:
		return HttpResponse(0)

#Por Katherine
def ajax_ubicacion(request):
	if request.method == 'POST':
		if request.POST.get('bandera') == 'd':
			data = list(Municipio.objects.filter(departamento=request.POST.get('id')).extra(select={'text': 'descripcion'}).values('text','id'))
		elif request.POST.get('bandera') == 'm':
			data = list(Aldea.objects.filter(municipio=request.POST.get('id')).extra(select={'text': 'descripcion'}).values('text','id'))
		elif request.POST.get('bandera') == 'a':
			data= list(Caserio.objects.filter(aldea=request.POST.get('id')).extra(select={'text': 'descripcion'}).values('text','id'))
		elif request.POST.get('bandera') == 'c':
			data= list(Barrio.objects.filter(caserio=request.POST.get('id')).extra(select={'text': 'descripcion'}).values('text','id'))
		print data

		return HttpResponse(json.dumps(data))
	else:
		return HttpResponse(0)
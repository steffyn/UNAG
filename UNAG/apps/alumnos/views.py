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
	check_password, make_password, PBKDF2PasswordHasher,
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

#Por Katherine
from django.shortcuts import render
import xlrd
import xlwt
from django.utils.encoding import smart_str, smart_unicode
from django.db import transaction
import os

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
#Sarai
def view_add_people_alu(request):
	#si esta autenticado desloguearlo porque entonces no es un aspirante el que ingresa
	if request.user.is_authenticated():
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.descripcion == 'Alumno':
			return HttpResponseRedirect(reverse('vista_main_administration')) 
		else:
			logout(request)
			return HttpResponseRedirect(reverse('vista_nuevo_primer_ingreso')) 
    #if request.user.is_authenticated():
    	#logout(request)
	
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
			user = User.objects.create_user(num_cuenta, formulario.cleaned_data['correo_electronico'],  make_password(random_number, 'seasalt', 'pbkdf2_sha256'))
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
		persona_id=Persona.objects.get(usuario_id=request.user.id).id
		return HttpResponseRedirect(reverse('vista_index_alumno'))
	except Persona.DoesNotExist:
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
				objPersona = Persona.objects.get(usuario_id = request.user.id)
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
				objPersona = Persona.objects.get(usuario_id = request.user.id)
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
			persona_id=Persona.objects.get(usuario_id=request.user.id).id
			if request.method == 'POST':
				if Alumnos.objects.filter(persona_id=persona_id): # si hay persona y hay alumno
					objAlumno = Alumnos.objects.get(persona_id=persona_id)
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
						form.persona=Persona.objects.get(usuario_id=request.user.id)
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
				if Alumnos.objects.filter(persona_id=persona_id): # si hay persona y hay alumno
					objAlumno = Alumnos.objects.get(persona_id=persona_id)
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
		persona_id=Persona.objects.get(usuario_id=request.user.id).id
	except Persona.DoesNotExist:
		return HttpResponseRedirect(reverse('vista_nuevo_reingreso'))

	ctx=[]
	try:
		persona_id=Persona.objects.get(usuario_id=request.user.id).id
		print persona_id
		alumno=Alumnos.objects.get(persona_id=persona_id)
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



#Incluida Katherine
@permission_required('alumnos.add_alumnos', login_url='/censo/logout/')
def alumno_registro_excel(request):
	#rarfile.UNRAR_TOOL = 'C:\Windows\unrar.exe' #esta configuracion es importante para el unrar
	context = {}
	if request.method == 'POST':
		form = FormArchivosGuardados(request.POST, request.FILES)
		flag = True
		error = []

		if form.is_valid():
			filename = request.FILES['archivo'].name
			if filename.endswith('.xlsm') != True and filename.endswith('.xlsx') != True:
				error.append(u'El archivo ingresado es el incorrecto, El archivo debe ser extension XLSM.')
				form = FormArchivosGuardados()
				context = {'errores':error, 'form':form}
			else:
				registro = form.save(commit=False)
				registro.usuario_creador = User.objects.get(id=request.user.id)
				registro.save()
				filename, file_extension = os.path.splitext(registro.archivo.path)

				book = xlrd.open_workbook(file_contents=registro.archivo.read()) #abre el archivo de excel
				sh = book.sheet_by_index(0) #toma la primera hoja de excel
				row_comienza = 10 #La fila donde comienzan los datos

				#validacion carrera
				carreras = sh.cell_value(3, 1)
				if carreras == '':
					flag = False
					error.append(u'La carrera no puede estar vacia.')
				else:
					try:
						carreras = Carrera.objects.get(nombre_carrera=smart_str(unicode(carreras)))
					except Exception, e:
						print 'pase por aqui4'
						flag = False
						error.append(u'La carrera elegida no se encuentra ingresada en la base de datos.')

				#validacion de las clases
				clase = sh.cell_value(4, 1)
				if clase == '':
					flag = False
					error.append(u'La clase no puede estar vacia.')
				else:
					try:
						clase = int(str(clase))
						flag = False
						error.append(u'La clase debe ser un número.')
					except Exception, e:
						pass

				#validacion del periodo
				periodo = sh.cell_value(5, 1)
				if periodo == '':
					flag = False
					error.append(u'El periodo no puede estar vacia.')

				if flag == False: # si es falso, pues errores
					form = FormArchivosGuardados()
					context = {'errores':error, 'form':form}
				elif flag == True:
					#Arreglos Necesarios
					no_ingresan = []
					ingresan = []
					registros_ingresados = [] #esta variables solamente es informativa, para mostrar al usuario los usuarios que se almacenaron

					for row in range(row_comienza, sh.nrows): #recorre todas las filas
						col_comienza = 0 #la columna donde comienzan los datos
						col_termina = 25 #la columna donde terminan los datos
						motivos = []

						#Validadcion Identidad
						identidad =  str(sh.cell_value(row, 1))
						if len(identidad) > 18:
							flag = False
							motivos.append(u'El número de Identidad no puede ser más 18 dígitos.')
						elif identidad == "":
							flag = False
							motivos.append(u'El número de Identidad no puede ser estar vacio.')

						#validacion tipo de identidad
						identificacion = sh.cell_value(row_comienza, 2)
						if identificacion == "":
							flag = False
							motivos.append(u'El tipo de identificación no puede estar vacio.')
						else:
							try:
								identificacion= TipoIdentificacion.objects.get(descripcion=str(identificacion))
							except Exception, e:
								flag = False
								motivos.append(u'El tipo de identificación no es correcta.')

						#Validacion de Genero
						genero = str(sh.cell_value(row_comienza, 6))
						if genero not in ('F', 'M'):
							flag = False
							motivos.append(u'El genero seleccionado es incorrecto. Solo puede elegir entre F: Femenino, M: Masculino')
						elif genero == "":
							flag = False
							motivos.append(u'El genero no puede estar vacio.')

						#validacion estado civil
						estado_civil = sh.cell_value(row_comienza, 7)
						if estado_civil == "":
							flag = False
							motivos.append(u'El estado civil no puede estar vacio.')
						else:
							try:
								estado_civil=EstadoCivil.objects.get(descripcion=Estado_civil)
							except Exception, e:
								flag = False
								motivos.append(u'El estado civil que se eligio no se encuentra almacenado en el sistema.')

						#validacion direccion
						direccion = str(sh.cell_value(row_comienza, 8))
						if direccion == "":
							flag = False
							motivos.append(u'La direccion no puede estar vacio.')

						#validacion correo electronico
						correo_electronico = str(sh.cell_value(row_comienza, 9))
						if correo_electronico == "":
							flag = False
							motivos.append(u'El correo electrónico no puede estar vacio.')
						else:
							try:
								alumno = Alumnos.objects.get(correo_electronico=correo_electronico)
							except Exception, e:
								pass
							else:
								if alumno.persona.identidad != identidad:
									flag = False
									motivos.append(u'El correo ingresado está asignado a otro alumno.')

						#validacion de telefonos
						try:
							celular = str(int(sh.cell_value(row_comienza, 10)))
							if len(celular) > 8:
								flag = False
								motivos.append(u'El número de celular no puede ser más largo de 8 dígitos')
						except Exception, e:
							if str(sh.cell_value(row_comienza, 10)) == "":
								flag = False
								motivos.append(u'El celular no puede estar vacio.')
							else:
								flag = False
								motivos.append(u'El celular debe de ser un número.')

						try:
							telefono_fijo = str(int(sh.cell_value(row_comienza, 11)))
							if len(telefono_fijo) > 8:
								flag = False
								motivos.append(u'El teléfono fijo no puede ser más largo de 8 dígitos')
						except Exception, e:
							flag = False
							motivos.append(u'El teléfono fijo debe de ser un número.')

						#validacion de los paises
						pais_nacimiento = sh.cell_value(row_comienza, 12)
						pais_residencia = sh.cell_value(row_comienza, 13)

						if pais_nacimiento=="" or pais_residencia=="":
							flag = False
							motivos.append(u'El país de residencia y el país de nacimiento no pueden estar vacio.')
						else:
							try:
								pais_nacimiento = Pais.objects.get(descripcion=pais_nacimiento)
							except Exception, e:
								flag= False
								motivos.append(u'El país de residencia seleccionado no se encuentra ingresado en el sistema.')

							try:
								pais_residencia = Pais.objects.get(descripcion=pais_residencia)
							except Exception, e:
								flag= False
								motivos.append(u'El país de residencia seleccionado no se encuentra ingresado en el sistema.')

						#validacion de tipo de persona
						tipo_Persona = sh.cell_value(row_comienza, 14)
						if tipo_Persona=="":
							flag = False
							motivos.append(u'El tipo de persona no puede estar vacio.')
						else:
							try:
								tipo_persona = TipoPersona.objects.get(descripcion=TipoPersona)
							except Exception, e:
								flag= False
								motivos.append(u'El tipo de persona seleccionado no se encuentra ingresado en el sistema.')

						#validacion zona
						zona = sh.cell_value(row_comienza, 15)
						if zona=="":
							flag = False
							Zona = motivos.append(u'La zona no puede estar vacia.')
						else:
							try:
								zona = Zona.objects.get(descripcion=Zona)
							except Exception, e:
								flag= False
								motivos.append(u'La zona seleccionada no se encuentra ingresado en el sistema.')

						#validacion promedio de graduacion
						promedio_graduacion = sh.cell_value(row_comienza, 18)
						if promedio_graduacion=="":
							flag = False
							motivos.append(u'El promedio de graduacion no puede estar vacio.')

						#validacion nombre del padre
						nombre_padre = sh.cell_value(row_comienza, 19)
						if nombre_padre=="":
							flag = False
							motivos.append(u'El nombre del Padre o Encargado no puede estar vacio.')

						#validacion profesion del padre
						profesion_padre = sh.cell_value(row_comienza, 20)
						if profesion_padre =="":
							flag = False
							motivos.append(u'El nombre del Padre o Encargado no puede estar vacio.')

						#validacion del telefono del padre
						telefono_padre = sh.cell_value(row_comienza, 21)
						try:
							telefono_padre = str(int(sh.cell_value(row_comienza, 21)))
							if len(telefono_padre) > 8:
								flag = False
								motivos.append(u'El número de télefono de la madre no puede ser más largo de 8 dígitos')
						except Exception, e:
							if  str(sh.cell_value(row_comienza, 21)) != "":
								flag = False
								motivos.append(u'El telefono del padre debe de ser un número.')

						#validacion del telefono de la madre
						telefono_madre = sh.cell_value(row_comienza, 25)
						try:
							telefono_madre = str(int(sh.cell_value(row_comienza, 25)))
							if len(telefono_madre) > 8:
								flag = False
								motivos.append(u'El número de télefono de la madre no puede ser más largo de 8 dígitos')
						except Exception, e:
							if  str(sh.cell_value(row_comienza, 25)) != "":
								flag = False
								motivos.append(u'El telefono del madre debe de ser un número.')

						#validacion tiene hijos
						tiene_hijos = sh.cell_value(row_comienza, 27)
						if tiene_hijos == "":
							flag = False
							motivos.append(u'El campo ¿Tiene hijos? no puede estar vacio.')
						elif tiene_hijos not in ('Si', 'No'):
							flag = False
							motivos.append(u'La opción escogida en el campo ¿Tiene Hijos? es Incorrecta.')

						#validacion Familiar
						try:
							posicion_familiar = int(sh.cell_value(row_comienza, 28))
						except Exception, e:
							if  str(sh.cell_value(row_comienza, 28)) != "":
								flag = False
								motivos.append(u'La posición familiar debe ser un número.')

						#validacion titulos
						titulos = sh.cell_value(row_comienza, 16)

						if titulos == '':
							flag = False
							motivos.append(u'El titulo no debe estar vacio.')
						else:
							try:
								lista_titulos = titulos.split("|")
								for x in lista_titulos:
									titule = Titulos.objects.get(descripcion=smart_str(unicode(x)))
							except Exception, e:
								flag = False
								motivos.append(u'Alguno de los titulos ingresados no se encuentra en el sistema.')
							else:
								try:
									Titulos.objects.get(descripcion=smart_str(unicode(titulos)))
								except Exception, e:
									flag = False
									motivos.append(u'El titulo ingresado no se encuentra en el sistema.')

						#validacion de titulos
						centros = sh.cell_value(row_comienza, 17)
						if centros == '':
							flag = False
							motivos.append(u'El centro educativo no debe estar vacio.')

						if centros == '':
							flag = False
							motivos.append(u'El centro educativo no debe estar vacio.')
						else:
							try:
								lista_centros = centros.split("|")
								for x in lista_centros:
									Centro.objects.get(descripcion=smart_str(unicode(x)))
							except Exception, e:
								try:
									Centro.objects.get(descripcion=smart_str(unicode(centros)))
								except Exception, e:
									flag = False
									motivos.append(u'Alguno de los centros ingresados no se encuentra en el sistema.')
						
						#validacion del codigo de registro
						codigo_registro = sh.cell_value(row_comienza, 0)
						try:
							alumno = Alumnos.objects.get(codigo_registro=codigo_registro)
						except Exception, e:
							pass
						else:
							if alumno.persona.identidad != identidad:
								flag = False
								motivos.append(u'El codígo de Registro ingresado está asignado a otro alumno.')
						
						#delaclaracion de las demas variables sin validaciones
						nombres = sh.cell_value(row_comienza, 3)
						apellidos = sh.cell_value(row_comienza, 4)
						asociacionPadre = sh.cell_value(row_comienza, 22)
						nombre_madre = sh.cell_value(row_comienza, 23)
						profesion_madre = sh.cell_value(row_comienza, 24)
						asociacionMadre = sh.cell_value(row_comienza, 26)
						observaciones = sh.cell_value(row_comienza, 29)
						usuario_creador = User.objects.get(id=request.user.id)

						#conversion de fecha
						if centros == '':
							flag = False
							motivos.append(u'La fecha de nacimiento no debe de ir vacia.')
						else:
							try:
								fecha_nacimiento = sh.cell_value(row_comienza, 5)
								tuple_date = xlrd.xldate_as_tuple(fecha_nacimiento, book.datemode)
								pydatetime = datetime(*tuple_date)
							except Exception, e:
								flag = False
								motivos.append(u'El formato de la fecha no es correcto (Año-Mes-Día).')

						if flag == False:
							no_ingresan.append({'fila':row_comienza,'identidad':identidad, 'nombres':nombres, 'apellidos': apellidos, 'motivos':motivos})
						else:
							#with transaction.atomic():
							# try:
							usuario, creado = User.objects.update_or_create(username =identidad)
							usuario.tipo_usuario = TipoUsuario.objects.get(pk=4)
							usuario.direccion = direccion
							usuario.telefono = celular
							usuario.set_password('registro')
							usuario.groups.add(Group.objects.get(name='Alumnos'))
							usuario.save()

							query_arg = {}
							query_arg['identidad'] = identidad
							query_arg['tipo_identificacion'] = identificacion
							query_arg['nombres'] = nombres
							query_arg['apellidos'] = apellidos
							query_arg['fecha_nacimiento'] = pydatetime
							query_arg['genero'] = genero
							query_arg['estado_civil'] = Estado_civil
							query_arg['direccion'] = direccion
							query_arg['correo_electronico'] = correo_electronico
							query_arg['celular'] = celular
							query_arg['telefono_fijo'] = telefono_fijo
							query_arg['pais_nacimiento'] = pais_nacimiento
							query_arg['pais_residencia'] = pais_residencia
							query_arg['tipo_persona'] = TipoPersona
							query_arg['zona'] = Zona
							query_arg['usuario'] = usuario
							query_arg['usuario_creador'] = usuario_creador
							query_arg['usuario_modificador'] = usuario_creador

							registro_persona, created = Persona.objects.update_or_create(identidad=identidad,defaults=query_arg)
							#registro_persona, created = persona.objects.update_or_create(identidad=identidad, defaults=query_arg)

							try:
								lista_titulos = titulos.split("|")
								for x in lista_titulos:
									registro_persona.titulos.add(Titulos.objects.get(descripcion=unicode(x)))
							except Exception, e:
								registro_persona.titulos.add(Titulos.objects.get(descripcion=unicode(titulo)))

							try:
								lista_centros = centros.split("|")
								for x in lista_centros:
									registro_persona.centros.add(Centro.objects.get(descripcion=smart_str(unicode(x))))
							except Exception, e:
								registro_persona.centros.add(Centro.objects.get(descripcion=smart_str(unicode(centros))))

							query_arg = {}
							query_arg['persona'] = registro_persona
							query_arg['promedio_graduacion'] = promedio_graduacion
							query_arg['nombre_padre'] = nombre_padre
							query_arg['profesion_padre'] = profesion_padre
							query_arg['telefono_padre'] = telefono_padre
							if asociacionPadre != '':
								query_arg['asoc_campesina_padre'] = asociacionPadre
							query_arg['nombre_madre'] = nombre_madre
							query_arg['profesion_madre'] = profesion_madre
							query_arg['telefono_madre'] = telefono_madre
							if asociacionMadre != '':
								query_arg['asoc_campesina_madre'] = asociacionMadre
							query_arg['correo_electronico'] = correo_electronico
							query_arg['tiene_hijos'] = tiene_hijos
							query_arg['posicion_familiar'] = posicion_familiar
							query_arg['observaciones'] = observaciones
							query_arg['codigo_registro'] = codigo_registro
							query_arg['usuario_creador'] = usuario_creador
							query_arg['usuario_modificador'] = usuario_creador
							registro_alumno, creado = Alumnos.objects.update_or_create(persona =registro_persona, defaults=query_arg)

							query_arg = {}
							query_arg['alumno'] = registro_alumno
							query_arg['carrera'] = carreras
							query_arg['clase'] = clase
							query_arg['periodo_academico'] = periodo
							query_arg['usuario_creador'] = usuario_creador
							query_arg['usuario_modificador'] = usuario_creador
							registro_promocion, creado = Promocion.objects.update_or_create(alumno =registro_alumno, defaults=query_arg)

							registros_ingresados.append({'fila':row_comienza,'identidad':identidad, 'nombres':nombres, 'apellidos': apellidos})
							# except Exception, e:
							# 	raise e
						#Si todo esta bien se agregan los alumnos a la base
						row_comienza += 1
					context = {'form':form, 'ingresan': registros_ingresados, 'no_ingresan': no_ingresan, 'bandera':True}
		else:
			error.append(u'Falta Archivo!!! Porfavor seleccione un archivo de Excel.')
			form = FormArchivosGuardados()
			context = {'errores':error, 'form':form}
	else:
		form = FormArchivosGuardados()
		context = {'form':form}
	return render(request, 'alumnos/registro_excel.html', context)


def alumno_registro(request):
	#si esta autenticado desloguearlo porque entonces no es un aspirante el que ingresa
	if request.user.is_authenticated():
		user = User.objects.get(id=request.user.id)
		if user.tipo_usuario.descripcion == 'alumno':
			return HttpResponseRedirect(reverse('vista_main_administration'))
    #if request.user.is_authenticated():
    	#logout(request)
	
	mensaje=''
	exito = ''
	alumno = ''
	if request.method == 'POST':
		formulario = AspirantePersonaForm(request.POST, request.FILES) 
		formulario_alu = AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid() and formulario_alu.is_valid():
			num_cuenta=formulario.cleaned_data['identidad']
			#crear un usuario inact ivo para la persona
			user = User.objects.create_user(num_cuenta, formulario.cleaned_data['correo_electronico'], 'registro') #make_password(random_number, 'seasalt', 'pbkdf2_sha256')
			try:
				#crear persona
				person = formulario.save(commit = False)

				try:
					person.municipio = Municipio.objects.get(pk=request.POST['municipio'])
				except Exception, e:
					pass
				try:
					person.aldea =  Aldea.objects.get(pk=request.POST['aldea'])
				except Exception, e:
					pass
				try:
					person.caserio =  Caserio.objects.get(pk=request.POST['caserio'])
				except Exception, e:
					pass
				try:
					person.barrio = Barrio.objects.get(pk=request.POST['barrio'])
				except Exception, e:
					pass
		
				person.usuario = user
				person.usuario_creador = user
				person.fecha_creacion = datetime.now()
				person.usuario_modificador = user
				person.fecha_modificacion = datetime.now()
				person.save() #guardar persona

				#crear alumno
				form = formulario_alu.save(commit = False)
				form.persona=person
				form.usuario_creador = user
				form.fecha_creacion = datetime.now()
				form.usuario_modificador = user
				form.fecha_modificacion = datetime.now()
				form.save()

				# guardar many to many fields
				formulario.save_m2m()
				formulario_alu.save_m2m()

				#actualizar datos de usuario
				user.first_name=formulario.cleaned_data['nombres']
				user.last_name=formulario.cleaned_data['apellidos']
				user.is_staff=False
				user.is_active=False
				user.is_superuser=False
				user.groups.add(Group.objects.get(id=2))
				user.tipo_usuario=TipoUsuario.objects.get(id=10)
				user.date_joined=datetime.now()
				user.save()

				exito = 'El Registro se guardó con éxito'
				alumno = person

			except Exception, e:
				User.objects.filter(id=user.id).delete()
				person.delete()
				mensaje='Ocurrió un error al guardar favor inténtelo nuevamente'
				raise e
		else:
			mensaje="Formulario contiene errores"
	else:
		formulario = AspirantePersonaForm()
		formulario_alu = AlumnoForm()
	return render_to_response('alumnos/registro.html', {'formulario':formulario, 'formulario_alu':formulario_alu, 'mensaje':mensaje, 'exito':exito, 'alumno':alumno}, context_instance=RequestContext(request))

def alumno_lista(request):
	contexto = { 'alumnos' : Alumnos.objects.filter(estado=True) }
	return render(request,'alumnos/lista.html', contexto)


def alumno_editar(request, id=None):
	alumno = Alumnos.objects.get(pk=id)
	if request.method == 'POST':
		formulario_persona = PersonaAlumnoEditForm(request.POST,instance = alumno.persona)
		formulario_alumno = AlumnoForm(request.POST,instance = alumno)
		if formulario_persona.is_valid() and formulario_alumno.is_valid():
			formulario_persona.save()
			formulario_alumno.save()
			return HttpResponseRedirect(reverse('alumno_lista'))
		else:
			ctx = {'persona': formulario_persona, 'alumno': formulario_alumno, 'id':id}
			return render(request, 'alumnos/editar.html', ctx)
	else:
		formulario_persona = PersonaAlumnoEditForm(instance = alumno.persona)
		formulario_alumno = AlumnoForm(instance = alumno)
		ctx = {'persona': formulario_persona, 'alumno': formulario_alumno, 'id':id}
		return render(request, 'alumnos/editar.html', ctx)

def alumno_eliminar(request, id=None):
	if id:
		try:
			alumno = Alumnos.objects.get(pk=id)
			alumno.estado = False
			alumno.save()

			usuario = User.objects.get(username = alumno.persona.identidad)
			usuario.is_active = False
			usuario.save()
		except Exception, e:
			raise e
		

		print 'PASO POR AQUI'
		return HttpResponseRedirect(reverse('alumno_lista'))	
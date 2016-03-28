#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin

from UNAG.apps.general.models import *
#from UNAG.apps.alumnos.models import *


# Create your models here.
class Documentos(models.Model):
	cod_documento=models.CharField(max_length=32, error_messages={'unique':u'Ya existe un Documento con este Código.'}, help_text="Ingrese un código que identifique el documento",unique=True)
	descripcion=models.CharField(max_length=1024)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='doc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='doc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	
	class Meta:
		db_table = 'registro_documentos'

	def __unicode__(self):
		return self.descripcion

class  TiposCondicionesMatricula(models.Model):
	descripcion=models.CharField(max_length=1024, unique=True)
	acciones_condicion=models.CharField(max_length=2048)
	usuario_creador=models.ForeignKey(User, related_name='cm_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='cm_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_tipo_condiciones_matricula'

	def __unicode__(self):
		return self.descripcion


class DepartamentoAcademico(models.Model):
	codigo =models.CharField(max_length=28)
	descripcion=models.CharField(max_length=512)
	id_campus=models.ForeignKey(Campus)
	jefe=models.ForeignKey(Persona, null=True, blank = True, default = None)
	cod_usuario_creador=models.ForeignKey(User,related_name="fk_usuario_deptoa")
	fecha_creacion=models.DateField(auto_now_add=True)
	cod_usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_deptoa_1")
	fecha_modificacion=models.DateField(auto_now=True)
	
	class Meta:
		db_table = 'registro_departamento_academico'
		unique_together = ('codigo','id_campus')

	def __unicode__(self):
		return self.descripcion

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'id_campus'):
			return 'Ya existe Departamento académico con el mismo Código y Campus.'
		else:
			return super(DepartamentoAcademico, self).unique_error_message(model_class, unique_check)


class Carrera(models.Model):
	Modalidad_CHOICES = (('INTERNADO', 'Internado'),('EXTERNADO', 'Externado'))
	codigo =models.CharField(max_length=32, verbose_name='Código', unique=True)
	nombre_carrera=models.CharField(max_length=256)
	siglas_carrera=models.CharField(max_length=15)
	duracion=models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Duración', help_text='Ingrese la duración en años. Ej. Si una carrera dura 4 años y medio ingrese 4.5')
	modalidad=models.CharField(choices=Modalidad_CHOICES, verbose_name='Modalidad', max_length=30)
	#modalidad=models.ForeignKey(modalidades)
	persona_responsable=models.ForeignKey(Persona)
	campus=models.ForeignKey(Campus)
	grado=models.ForeignKey(GrupoGrado)
	depto_academico=models.ForeignKey(DepartamentoAcademico)
	fecha_aprobacion=models.DateField(verbose_name='Fecha de aprobación')
	cant_uv =models.IntegerField()
	cant_asignaturas= models.IntegerField()
	cant_laboratorios=models.IntegerField()
	uv_laboratorios=models.IntegerField()
	uv_pps=models.IntegerField()
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)
	observaciones=models.TextField(max_length=1024)

	class Meta:
		db_table = 'registro_carrera'
		unique_together = ('codigo','campus')

	def __unicode__(self):
		return self.nombre_carrera

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'campus'):
			return 'Ya existe una Carrera con el mismo Código y Campus.'
		else:
			return super(Carrera, self).unique_error_message(model_class, unique_check)

### models josue

class TipoAsignatura(models.Model):
	descripcion=models.CharField(max_length=512, unique=True)
	nota_aprobatorio=models.DecimalField(max_digits=4, decimal_places=0)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='tasi_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tasi_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_tipo_asignatura'

	def __unicode__(self):
		return self.descripcion




class Asignatura(models.Model):
	codigo_registro=models.CharField(max_length=512, unique=True)
	nombre_asignatura=models.CharField(max_length=1024)
	carrera=models.ForeignKey(Carrera, verbose_name='Carrera')
	tipo_asignatura=models.ForeignKey(TipoAsignatura, related_name='tasi_asi_tipo_asignatura')
	uv=models.IntegerField(verbose_name='Unidades valorativas')
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='asig_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='asig_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	
	class Meta:
		db_table = 'registro_asignatura'
		unique_together = ('codigo_registro','nombre_asignatura')

	def __unicode__(self):
		return self.nombre_asignatura

class Modulo(models.Model):
	carrera=models.ForeignKey(Carrera)
	laboratorio=models.ForeignKey(Asignatura,  related_name='laboratorio_id', verbose_name='laboratorios', unique=True)
	modulo=models.ForeignKey(Asignatura, related_name='modulo_id')
	usuario_creador=models.ForeignKey(User, related_name='mod_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='mod_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_modulo'


class TipoDocente(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='tdoc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tdoc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_tipo_docente'

	def __unicode__(self):
		return self.descripcion                                                                 

class JornadaLaboral(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='jlab_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='jlab_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_jornada_laboral'
	
	def __unicode__(self):
		return self.descripcion

class docente_departamento(models.Model):
	persona=models.ForeignKey(Persona)
	campus=models.ForeignKey(Campus)
	jornada=models.ManyToManyField(Jornada)
	jornada_laboral=models.ForeignKey(JornadaLaboral)
	departamento_academico=models.ForeignKey(DepartamentoAcademico, verbose_name='Departamento académico al que pertenece')
	tipo_docente=models.ForeignKey(TipoDocente)
	fecha_inicio_laboral=models.DateField(auto_now_add=True ,verbose_name='Fecha en que inició a laborar')
	activo=models.BooleanField()
	usuario_creador=models.ForeignKey(User, related_name='ddep_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ddep_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_docente_departamento'

	def __unicode__(self):
		return self.persona



		
class Seccion(models.Model):
	descripcion=models.CharField(max_length=512)
	periodo_clase=models.ForeignKey(PeriodoClase)
	jornada=models.ForeignKey(Jornada)
	carrera=models.ForeignKey(Carrera)
	aula=models.ForeignKey(EstructuraEdificio)
	usuario_creador=models.ForeignKey(User, related_name='sec_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='sec_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def _get_full_seccion(self):
		"Returns the person's full name."
		return '%s | %s | %s' % (self.descripcion, self.jornada, self.carrera)
	full_seccion = property(_get_full_seccion)

	def __unicode__(self):
		return self.full_seccion

	class Meta:
		db_table = 'registro_seccion'
		unique_together = ('descripcion', 'carrera', 'periodo_clase', 'jornada')
		unique_together = ('descripcion', 'carrera', 'periodo_clase')
		unique_together = ('jornada', 'carrera', 'periodo_clase', 'aula')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('descripcion', 'carrera', 'periodo_clase', 'jornada'):
			return 'Ya existe una Seccion con la misma descripción en la misma carrera y período.'
		else:
			return super(seccion, self).unique_error_message(model_class, unique_check)


class Horario(models.Model):
	seccion=models.ForeignKey(Seccion)
	descripcion=models.CharField(max_length=128)
	usuario_creador=models.ForeignKey(User, related_name="fk_usuario_horario")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_horario_1")
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_horario'

	def __unicode__(self):
		return self.descripcion

class HorarioHora(models.Model):
	horario=models.ForeignKey(Horario)
	hora_inicial=models.TimeField()
	hora_final=models.TimeField()
	usuario_creador=models.ForeignKey(User, related_name='hhor_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='hhor_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'registro_horario_hora'

class AsignaturaSeccion(models.Model):
	Dias_CHOICES = (('Lun', 'Lunes'),('Mar', 'Martes'),('Mie', 'Miercoles'),('Jue', 'Jueves'),('Vie', 'Viernes'),('Sab', 'Sabado'),('Dom', 'Domingo'))
	asignatura=models.ForeignKey(Asignatura)
	#edificio=models.ForeignKey(edificios)
	#cupos=models.IntegerField()
	horario_hora=models.ForeignKey(HorarioHora)
	dia=models.CharField(max_length=3, choices=Dias_CHOICES)
	#seccion=models.ForeignKey(seccion)
	docente_carrera=models.ForeignKey(docente_departamento, verbose_name='Docente')
	usuario_creador=models.ForeignKey(User, related_name='asec_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='asec_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'registro_asignatura_seccion'


class AsignaturaBloque(models.Model):
	asignatura=models.ForeignKey(Asignatura)
	bloque=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ablo_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ablo_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'registro_asignatura'

class Parcial(models.Model):
	periodo_clase=models.ForeignKey(PeriodoClase)
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='parc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='parc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'registro_parcial'

#by ciloe 04 - octubre -2013 creacion de la tabla requisito
class Requisito(models.Model):
	asignatura_base=models.ForeignKey(Asignatura,related_name='req_asignatura_base')
	asignatura_requisito=models.ForeignKey(Asignatura,related_name='req_asignatura_requisito')
	usuario_creador=models.ForeignKey(User, related_name='req_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='req_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)	
	class Meta:
		db_table = 'registro_requisito'	

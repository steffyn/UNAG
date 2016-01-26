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

class documentos(models.Model):
	cod_documento=models.CharField(max_length=32, error_messages={'unique':u'Ya existe un Documento con este Código.'}, help_text="Ingrese un código que identifique el documento",unique=True)
	descripcion=models.CharField(max_length=1024)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='doc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='doc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class  tipos_condiciones_matricula(models.Model):
	descripcion=models.CharField(max_length=1024, unique=True)
	acciones_condicion=models.CharField(max_length=2048)
	usuario_creador=models.ForeignKey(User, related_name='cm_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='cm_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion


class departamento_academico(models.Model):
	codigo =models.CharField(max_length=28)
	descripcion=models.CharField(max_length=512)
	id_campus=models.ForeignKey(campus)
	jefe=models.ForeignKey(persona, null=True, blank = True, default = None)
	cod_usuario_creador=models.ForeignKey(User,related_name="fk_usuario_deptoa")
	fecha_creacion=models.DateField(auto_now_add=True)
	cod_usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_deptoa_1")
	fecha_modificacion=models.DateField(auto_now=True)
	

	class Meta:
		unique_together = ('codigo','id_campus')

	def __unicode__(self):
		return self.descripcion

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'id_campus'):
			return 'Ya existe Departamento académico con el mismo Código y Campus.'
		else:
			return super(departamento_academico, self).unique_error_message(model_class, unique_check)


class carrera(models.Model):
	Modalidad_CHOICES = (('INTERNADO', 'Internado'),('EXTERNADO', 'Externado'))
	codigo =models.CharField(max_length=32, verbose_name='Código', unique=True)
	nombre_carrera=models.CharField(max_length=256)
	siglas_carrera=models.CharField(max_length=15)
	duracion=models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Duración', help_text='Ingrese la duración en años. Ej. Si una carrera dura 4 años y medio ingrese 4.5')
	modalidad=models.CharField(choices=Modalidad_CHOICES, verbose_name='Modalidad', max_length=30)
	#modalidad=models.ForeignKey(modalidades)
	persona_responsable=models.ForeignKey(persona)
	campus=models.ForeignKey(campus)
	grado=models.ForeignKey(grupo_grado)
	depto_academico=models.ForeignKey(departamento_academico)
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
		unique_together = ('codigo','campus')

	def __unicode__(self):
		return self.nombre_carrera

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'campus'):
			return 'Ya existe una Carrera con el mismo Código y Campus.'
		else:
			return super(carrera, self).unique_error_message(model_class, unique_check)

### models josue

class tipo_asignatura(models.Model):
	descripcion=models.CharField(max_length=512, unique=True)
	nota_aprobatorio=models.DecimalField(max_digits=4, decimal_places=0)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='tasi_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tasi_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class asignatura(models.Model):
	codigo_registro=models.CharField(max_length=512, unique=True)
	nombre_asignatura=models.CharField(max_length=1024)
	carrera=models.ForeignKey(carrera, verbose_name='Carrera')
	tipo_asignatura=models.ForeignKey(tipo_asignatura, related_name='tasi_asi_tipo_asignatura')
	uv=models.IntegerField(verbose_name='Unidades valorativas')
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='asig_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='asig_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		unique_together = ('codigo_registro','nombre_asignatura')

	def __unicode__(self):
		return self.nombre_asignatura

class tipo_docente(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='tdoc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tdoc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class jornada_laboral(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='jlab_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='jlab_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class docente_departamento(models.Model):
	persona=models.ForeignKey(persona)
	campus=models.ForeignKey(campus)
	jornada=models.ManyToManyField(jornada)
	jornada_laboral=models.ForeignKey(jornada_laboral)
	departamento_academico=models.ForeignKey(departamento_academico, verbose_name='Departamento académico al que pertenece')
	tipo_docente=models.ForeignKey(tipo_docente)
	fecha_inicio_laboral=models.DateField(auto_now_add=True ,verbose_name='Fecha en que inició a laborar')
	activo=models.BooleanField()
	usuario_creador=models.ForeignKey(User, related_name='ddep_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ddep_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.persona

class modulo(models.Model):
	tipo_asignatura=models.ForeignKey(tipo_asignatura)
	descripcion=models.CharField(max_length=512)
	periodo_clase=models.ForeignKey(periodo_clase)
	docente_carrera=models.ForeignKey(docente_departamento)
	usuario_creador=models.ForeignKey(User, related_name='mod_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='mod_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

class seccion(models.Model):
	descripcion=models.CharField(max_length=512)
	periodo_clase=models.ForeignKey(periodo_clase)
	jornada=models.ForeignKey(jornada)
	carrera=models.ForeignKey(carrera)
	aula=models.ForeignKey(estructura_edificio)
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
		unique_together = ('descripcion', 'carrera', 'periodo_clase', 'jornada')
		unique_together = ('descripcion', 'carrera', 'periodo_clase')
		unique_together = ('jornada', 'carrera', 'periodo_clase', 'aula')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('descripcion', 'carrera', 'periodo_clase', 'jornada'):
			return 'Ya existe una Seccion con la misma descripción en la misma carrera y período.'
		else:
			return super(seccion, self).unique_error_message(model_class, unique_check)


class horario(models.Model):
	seccion=models.ForeignKey(seccion)
	descripcion=models.CharField(max_length=128)
	usuario_creador=models.ForeignKey(User, related_name="fk_usuario_horario")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_horario_1")
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class horario_hora(models.Model):
	horario=models.ForeignKey(horario)
	hora_inicial=models.TimeField()
	hora_final=models.TimeField()
	usuario_creador=models.ForeignKey(User, related_name='hhor_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='hhor_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

class asignatura_seccion(models.Model):
	Dias_CHOICES = (('Lun', 'Lunes'),('Mar', 'Martes'),('Mie', 'Miercoles'),('Jue', 'Jueves'),('Vie', 'Viernes'),('Sab', 'Sabado'),('Dom', 'Domingo'))
	asignatura=models.ForeignKey(asignatura)
	#edificio=models.ForeignKey(edificios)
	#cupos=models.IntegerField()
	horario_hora=models.ForeignKey(horario_hora)
	dia=models.CharField(max_length=3, choices=Dias_CHOICES)
	#seccion=models.ForeignKey(seccion)
	docente_carrera=models.ForeignKey(docente_departamento, verbose_name='Docente')
	usuario_creador=models.ForeignKey(User, related_name='asec_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='asec_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)


class asignatura_bloque(models.Model):
	asignatura=models.ForeignKey(asignatura)
	bloque=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ablo_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ablo_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

class parcial(models.Model):
	periodo_clase=models.ForeignKey(periodo_clase)
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='parc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='parc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)


#by ciloe 04 - octubre -2013 creacion de la tabla requisito
class requisito(models.Model):
	asignatura_base=models.ForeignKey(asignatura,related_name='req_asignatura_base')
	asignatura_requisito=models.ForeignKey(asignatura,related_name='req_asignatura_requisito')
	usuario_creador=models.ForeignKey(User, related_name='req_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='req_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)		

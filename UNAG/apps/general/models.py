#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from UNAG.apps.general.validators import *
#from UNAG.apps.alumnos.models import *
# Create your models here.

class tipo_persona(models.Model):
	descripcion=models.CharField(max_length=128)
	usuario_creador=models.ForeignKey(User, related_name='tp_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='tp_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class tipo_identificacion(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='td_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='td_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion


class grupo_grado(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class titulos(models.Model):
	grupo_grado=models.ForeignKey(grupo_grado)
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ti_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='ti_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class tipo_administracion(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ta_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='ta_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class estado_civil(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ecs_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='ecs_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class zona(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='zona_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='zona_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class pais(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='pais_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='pais_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class tipo_centro(models.Model):
	tipo_administracion=models.ForeignKey(tipo_administracion)
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='tc_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='tc_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class centro(models.Model):
	tipo_centro=models.ForeignKey(tipo_centro)
	zona=models.ForeignKey(zona)
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ce_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='ce_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class asoc_campesina(models.Model):
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ac_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='ac_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion


## models Cyndi

class  departamento(models.Model):
	codigo_departamento=models.CharField(max_length=4)
	descripcion=models.CharField(max_length=64)
	usuario_creador=models.ForeignKey(User, related_name='dep_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='dep_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return '%s | %s' % (self.codigo_departamento,self.descripcion)

	
class municipio(models.Model):
	codigo_municipio=models.CharField(max_length=4)
	departamento=models.ForeignKey(departamento)
	descripcion=models.CharField(max_length=64)
	usuario_creador=models.ForeignKey(User, related_name='mun_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='mun_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return '%s | %s' % (self.codigo_municipio,self.descripcion)


class aldea(models.Model):
	descripcion=models.CharField(max_length=250)
	municipio=models.ForeignKey(municipio)
	usuario_creador=models.ForeignKey(User, related_name='al_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='al_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class caserio(models.Model):
	descripcion =models.CharField(max_length=128)
	aldea=models.ForeignKey(aldea)
	usuario_creador=models.ForeignKey(User, related_name='cas_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='cas_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())


	def __unicode__(self):
		return self.descripcion

class barrio(models.Model):
	descripcion=models.CharField(max_length=128)
	caserio	= models.ForeignKey(caserio)
	usuario_creador=models.ForeignKey(User, related_name='bo_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='bo_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion


class periodo(models.Model):
	anio=models.IntegerField(verbose_name='Año', help_text='Debe ser un número entero correspondiente al año del período, Ej. 2014')
	descripcion=models.CharField(max_length=65)
	usuario_creador=models.ForeignKey(User, related_name='pr_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='pr_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class periodo_clase(models.Model):
	periodo=models.ForeignKey(periodo)
	descripcion=models.CharField(max_length=128)
	fecha_inicio=models.DateField(default=datetime.now())
	fecha_fin=models.DateField(default=datetime.now())
	habilitar_ingreso=models.BooleanField(default=True, verbose_name='Habilitar ingreso(Carga Académica)')
	usuario_creador=models.ForeignKey(User, related_name='pc_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='pc_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion


class financiador(models.Model):
	nombre_financiador=models.CharField(max_length=1024)
	direccion=models.CharField(max_length=1024)
	telefono=models.CharField(max_length=20)
	nombre_contacto = models.CharField(max_length=256)
	correo_electronico=models.CharField(max_length=256)
	observaciones=models.TextField(max_length=2024)
	usuario_creador=models.ForeignKey(User, related_name='fin_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='fin_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.nombre_financiador



class jornada(models.Model):
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='jor_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='jor_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())
	
	def __unicode__(self):
		return self.descripcion



class tipo_beca(models.Model):
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='tb_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='tb_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())
	
	def __unicode__(self):
		return self.descripcion

class persona(models.Model):
	Sexo_CHOICES = (('M', 'Masculino'),('F', 'Femenino'))
	identidad=models.CharField(max_length=18, unique = True)
	tipo_identificacion=models.ForeignKey(tipo_identificacion, verbose_name = "Tipo de identificación")
	nombres=models.CharField(max_length=256)
	apellidos=models.CharField(max_length=256)
	fecha_nacimiento=models.DateField(default=datetime.now(), verbose_name = "Fecha de nacimiento")
	genero=models.CharField(max_length=2, verbose_name = "Género", choices=Sexo_CHOICES)
	estado_civil=models.ForeignKey(estado_civil)
	direccion=models.CharField(max_length=2024, verbose_name = "Dirección")
	correo_electronico=models.EmailField(max_length=256, verbose_name = "Correo electrónico", help_text='Indique un correo electrónico válido. Formato correo@dominio.com', unique = True)
	celular=models.CharField(max_length=8, validators=[validar(tipo='telefono', longitud=8)],help_text=u'Ingrese el número sin guiones (-)')
	telefono_fijo=models.CharField(max_length=8, verbose_name = "Teléfono fijo", validators=[validar(tipo='telefono', longitud=8)] ,help_text=u'Ingrese el número sin guiones (-)', null = True, blank = True,default = None)
	fax=models.CharField(max_length=18, null=True, blank = True, default = None)
	pais_nacimiento=models.ForeignKey(pais, related_name='nac_pais_nacimiento')
	pais_residencia=models.ForeignKey(pais, related_name='res_pais_residencia')
	departamento=models.ForeignKey(departamento, null = True, blank = True, default = None)
	municipio=models.ForeignKey(municipio, null = True, blank = True, default = None)
	aldea=models.ForeignKey(aldea, null=True, blank = True, default = None)
	caserio=models.ForeignKey(caserio, verbose_name = "Caserío", null = True, blank = True, default = None)
	barrio=models.ForeignKey(barrio, null = True, blank = True,default = None)
	tipo_persona=models.ForeignKey(tipo_persona)
	zona=models.ForeignKey(zona)
	titulos=models.ManyToManyField(titulos, verbose_name = "Títulos Obtenidos", help_text=u'Seleccione en el lado derecho los títulos que desea agregar pulsando el boton (+),  ')
	centros=models.ManyToManyField(centro, verbose_name = "Centros de Estudio")
	usuario=models.OneToOneField(User, related_name='person_usuario_posee')
	usuario_creador=models.ForeignKey(User, related_name='per_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='per_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.nombres, self.apellidos)
	nombre_completo = property(_get_full_name)

	def __unicode__(self):
		return '( %s ) %s' % (self.identidad, self.nombre_completo)

class campus(models.Model):
	codigo =models.CharField(max_length=32, unique=True)
	descripcion=models.CharField(max_length=128)
	director_campus=models.ForeignKey(persona, null = True, blank = True, default = None, unique=True, error_messages={'unique':u'Este Director ya esta asignado a otro Campus.'})
	siglas=models.CharField(max_length=32, unique=True)
	direccion=models.CharField(max_length=256)
	telefono=models.CharField(max_length=8, help_text='Número de teléfono sin guiones (-)')
	usuario_creador=models.ForeignKey(User, related_name='cam_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='cam_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

	class Meta:
		unique_together = ('codigo','siglas')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'siglas'):
			return 'Ya existe un Campus con el mismo Código y Siglas.'
		else:           
			return super(campus, self).unique_error_message(model_class, unique_check)


class tipo_edificios(models.Model):
	
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='tedi_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='tedi_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class edificios(models.Model):
	
	codigo =models.CharField(max_length=32)
	nombre=models.CharField(max_length=256)
	ubicacion=models.CharField(max_length=512)
	capacidad_total_personas= models.IntegerField()
	tipo_edificio=models.ForeignKey(tipo_edificios)
	cantidad_dormitorios=models.IntegerField(verbose_name='Cantidad de espacios físicos', help_text='Especifique la cantidad de aulas, dormitorios, oficinas, laboratorios..., según el tipo de edificio seleccionado.')
	usuario_creador=models.ForeignKey(User, related_name='edi_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='edi_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())
	campus=models.ForeignKey(campus)

	def __unicode__(self):
		return  '%s | %s' % (self.nombre, self.tipo_edificio)

	class Meta:
		unique_together = ('codigo','campus')

	def _get_full_info(self):
		"Returns the person's full name."
		return '%s | %s | %s' % (self.nombre, self.tipo_edificio, self.campus)
	info_edificio = property(_get_full_info)

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'campus'):
			return 'Ya existe un Edificio con el mismo Código y Campus..'
		else:
			return super(edificios, self).unique_error_message(model_class, unique_check)

class modalidades(models.Model):

	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='moda_usuario_creador')
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User, related_name='moda_usuario_modificador')
	fecha_modificacion=models.DateField(default=datetime.now())

	def __unicode__(self):
		return self.descripcion

class estructura_edificio(models.Model):
	codigo=models.CharField(max_length=13)
	edificio=models.ForeignKey(edificios)
	descripcion=models.CharField(max_length=512, unique=True)
	capacidad_personas=models.IntegerField()
	ocupados=models.IntegerField(verbose_name='Cantidad ocupados', blank=True, null=True, default=None)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_carrera")
	fecha_creacion=models.DateField(default=datetime.now())
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_carrera_1")
	fecha_modificacion=models.DateField(default=datetime.now())

	class Meta:
		unique_together = ('codigo','edificio')

	def __unicode__(self):
		return  '%s | %s' % (self.descripcion, self.edificio)

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'edificio'):
			return 'Ya existe un Espacio con el mismo Código y Edificio.'
		else:
			return super(estructura_edificio, self).unique_error_message(model_class, unique_check)

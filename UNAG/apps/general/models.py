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

class TipoPersona(models.Model):
	descripcion=models.CharField(max_length=128)
	usuario_creador=models.ForeignKey(User, related_name='tp_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tp_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		db_table='general_tipo_persona'

class TipoIdentificacion(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='td_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='td_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_tipo_identificacion'

	def __unicode__(self):
		return self.descripcion


class GrupoGrado(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_grupo_grado'

	def __unicode__(self):
		return self.descripcion

class Titulos(models.Model):
	grupo_grado=models.ForeignKey(GrupoGrado)
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ti_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ti_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_titulos'

	def __unicode__(self):
		return self.descripcion

class TipoAdministracion(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ta_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ta_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_tipo_adinistracion'

	def __unicode__(self):
		return self.descripcion

class EstadoCivil(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='ecs_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ecs_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_estado_civil'

	def __unicode__(self):
		return self.descripcion

class Zona(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='zona_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='zona_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_zona'

	def __unicode__(self):
		return self.descripcion

class Pais(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='pais_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='pais_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_pais'

	def __unicode__(self):
		return self.descripcion

class TipoCentro(models.Model):
	tipo_administracion=models.ForeignKey(TipoAdministracion)
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='tc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_tipo_centro'

	def __unicode__(self):
		return self.descripcion

class Centro(models.Model):
	tipo_centro=models.ForeignKey(TipoCentro)
	zona=models.ForeignKey(Zona)
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ce_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ce_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_centro'

	def __unicode__(self):
		return self.descripcion

class AsocCampesina(models.Model):
	descripcion=models.CharField(max_length=1024)
	usuario_creador=models.ForeignKey(User, related_name='ac_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='ac_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	
	class Meta:
		db_table='general_asoc_campesina'

	def __unicode__(self):
		return self.descripcion


## models Cyndi

class  Departamento(models.Model):
	codigo_departamento=models.CharField(max_length=4)
	descripcion=models.CharField(max_length=64)
	usuario_creador=models.ForeignKey(User, related_name='dep_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='dep_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_departamento'

	def __unicode__(self):
		return '%s | %s' % (self.codigo_departamento,self.descripcion)

	
class Municipio(models.Model):
	codigo_municipio=models.CharField(max_length=4)
	departamento=models.ForeignKey(Departamento)
	descripcion=models.CharField(max_length=64)
	usuario_creador=models.ForeignKey(User, related_name='mun_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='mun_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_municipio'

	def __unicode__(self):
		return '%s | %s' % (self.codigo_municipio,self.descripcion)


class Aldea(models.Model):
	descripcion=models.CharField(max_length=250)
	municipio=models.ForeignKey(Municipio)
	usuario_creador=models.ForeignKey(User, related_name='al_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='al_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_aldea'


	def __unicode__(self):
		return self.descripcion

class Caserio(models.Model):
	descripcion =models.CharField(max_length=128)
	aldea=models.ForeignKey(Aldea)
	usuario_creador=models.ForeignKey(User, related_name='cas_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='cas_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_caserio'


	def __unicode__(self):
		return self.descripcion

class Barrio(models.Model):
	descripcion=models.CharField(max_length=128)
	caserio	= models.ForeignKey(Caserio)
	usuario_creador=models.ForeignKey(User, related_name='bo_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='bo_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_barrio'

	def __unicode__(self):
		return self.descripcion


class Periodo(models.Model):
	descripcion=models.CharField(max_length=65)
	usuario_creador=models.ForeignKey(User, related_name='pr_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='pr_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_periodo'

	def __unicode__(self):
		return self.descripcion

class PeriodoClase(models.Model):
	descripcion=models.CharField(max_length=128)
	periodo=models.ForeignKey(Periodo)
	usuario_creador=models.ForeignKey(User, related_name='pc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='pc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_periodo_clase'

	def __unicode__(self):
		return self.descripcion


class Financiador(models.Model):
	nombre_financiador=models.CharField(max_length=1024)
	direccion=models.CharField(max_length=1024)
	telefono=models.CharField(max_length=20)
	nombre_contacto = models.CharField(max_length=256)
	correo_electronico=models.CharField(max_length=256)
	observaciones=models.TextField(max_length=2024)
	usuario_creador=models.ForeignKey(User, related_name='fin_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='fin_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_financiador'

	def __unicode__(self):
		return self.nombre_financiador



class Jornada(models.Model):
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='jor_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='jor_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_jornada'
	
	def __unicode__(self):
		return self.descripcion



class TipoBeca(models.Model):
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='tb_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tb_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_tipo_beca'

	def __unicode__(self):
		return self.descripcion

class Persona(models.Model):
	Sexo_CHOICES = (('M', 'Masculino'),('F', 'Femenino'))
	identidad=models.CharField(max_length=18, unique = True)
	tipo_identificacion=models.ForeignKey(TipoIdentificacion, verbose_name = "Tipo de identificación")
	nombres=models.CharField(max_length=256)
	apellidos=models.CharField(max_length=256)
	fecha_nacimiento=models.DateField(verbose_name = "Fecha de nacimiento")
	genero=models.CharField(max_length=2, verbose_name = "Género", choices=Sexo_CHOICES)
	estado_civil=models.ForeignKey(EstadoCivil)
	direccion=models.CharField(max_length=2024, verbose_name = "Dirección")
	correo_electronico=models.EmailField(max_length=256, verbose_name = "Correo electrónico", help_text='Indique un correo electrónico válido. Formato correo@dominio.com', unique = True)
	celular=models.CharField(max_length=8,help_text=u'Ingrese el número sin guiones (-)')
	telefono_fijo=models.CharField(max_length=8, verbose_name = "Teléfono fijo", help_text=u'Ingrese el número sin guiones (-)', null = True, blank = True,default = None)
	fax=models.CharField(max_length=18, null=True, blank = True, default = None)
	pais_nacimiento=models.ForeignKey(Pais, related_name='nac_pais_nacimiento')
	pais_residencia=models.ForeignKey(Pais, related_name='res_pais_residencia')
	departamento=models.ForeignKey(Departamento, null = True, blank = True, default = None)
	municipio=models.ForeignKey(Municipio, null = True, blank = True, default = None)
	aldea=models.ForeignKey(Aldea, null=True, blank = True, default = None)
	caserio=models.ForeignKey(Caserio, verbose_name = "Caserío", null = True, blank = True, default = None)
	barrio=models.ForeignKey(Barrio, null = True, blank = True,default = None)
	tipo_persona=models.ForeignKey(TipoPersona)
	zona=models.ForeignKey(Zona)
	titulos=models.ManyToManyField(Titulos, verbose_name = "Títulos Obtenidos", help_text=u'Seleccione en el lado derecho los títulos que desea agregar pulsando el boton (+),  ')
	centros=models.ManyToManyField(Centro, verbose_name = "Centros de Estudio")
	usuario=models.OneToOneField(User, related_name='person_usuario_posee')
	usuario_creador=models.ForeignKey(User, related_name='per_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='per_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_persona'

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.nombres, self.apellidos)
	nombre_completo = property(_get_full_name)

	def __unicode__(self):
		return '( %s ) %s' % (self.identidad, self.nombre_completo)

class Campus(models.Model):
	codigo =models.CharField(max_length=32, unique=True)
	descripcion=models.CharField(max_length=128)
	director_campus=models.OneToOneField(Persona, null = True, blank = True, default = None, unique=True, error_messages={'unique':u'Este Director ya esta asignado a otro Campus.'})
	siglas=models.CharField(max_length=32, unique=True)
	direccion=models.CharField(max_length=256)
	telefono=models.CharField(max_length=8, help_text='Número de teléfono sin guiones (-)')
	usuario_creador=models.ForeignKey(User, related_name='cam_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='cam_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		db_table='general_campus'
		unique_together = ('codigo','siglas')

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'siglas'):
			return 'Ya existe un Campus con el mismo Código y Siglas.'
		else:
			return super(Campus, self).unique_error_message(model_class, unique_check)


class TipoEdificios(models.Model):
	
	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='tedi_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tedi_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_tipo_edificios'

	def __unicode__(self):
		return self.descripcion

class Edificios(models.Model):
	
	codigo =models.CharField(max_length=32)
	nombre=models.CharField(max_length=256)
	ubicacion=models.CharField(max_length=512)
	capacidad_total_personas= models.IntegerField()
	tipo_edificio=models.ForeignKey(TipoEdificios)
	cantidad_dormitorios=models.IntegerField(verbose_name='Cantidad de espacios físicos', help_text='Especifique la cantidad de aulas, dormitorios, oficinas, laboratorios..., según el tipo de edificio seleccionado.')
	usuario_creador=models.ForeignKey(User, related_name='edi_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='edi_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	campus=models.ForeignKey(Campus)

	def __unicode__(self):
		return  '%s | %s' % (self.nombre, self.tipo_edificio)

	class Meta:
		db_table='general_edificios'
		unique_together = ('codigo','campus')

	def _get_full_info(self):
		"Returns the person's full name."
		return '%s | %s | %s' % (self.nombre, self.tipo_edificio, self.campus)
	info_edificio = property(_get_full_info)

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'campus'):
			return 'Ya existe un Edificio con el mismo Código y Campus..'
		else:
			return super(Edificios, self).unique_error_message(model_class, unique_check)

class Modalidades(models.Model):

	descripcion=models.CharField(max_length=256)
	usuario_creador=models.ForeignKey(User, related_name='moda_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='moda_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_modalidades'

	def __unicode__(self):
		return self.descripcion

class EstructuraEdificio(models.Model):
	codigo=models.CharField(max_length=13)
	edificio=models.ForeignKey(Edificios)
	descripcion=models.CharField(max_length=512, unique=True)
	capacidad_personas=models.IntegerField()
	ocupados=models.IntegerField(verbose_name='Cantidad ocupados', blank=True, null=True, default=None)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_carrera")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_carrera_1")
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='general_estructura_edificio'
		unique_together = ('codigo','edificio')

	def __unicode__(self):
		return  '%s | %s' % (self.descripcion, self.edificio)

	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('codigo', 'edificio'):
			return 'Ya existe un Espacio con el mismo Código y Edificio.'
		else:
			return super(EstructuraEdificio, self).unique_error_message(model_class, unique_check)



#Por Katherine
def url(obj, filename):
	    ruta = "documentos/%s/%s"%(obj.usuario_creador, obj.archivo)
	    return ruta

class archivos_guardados(models.Model):
	archivo = models.FileField(upload_to=url)
	usuario_creador = models.ForeignKey(User)
	fecha_creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.archivo
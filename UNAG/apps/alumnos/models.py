#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin

from UNAG.apps.general.models import *
from UNAG.apps.registro.models import *
from UNAG.apps.general.validators import *
# Create your models here.

class Alumnos(models.Model):
	persona=models.ForeignKey(Persona)
	promedio_graduacion=models.DecimalField(max_digits=5, verbose_name=u'Promedio de graduacion (Obtenido en diversificado)', decimal_places=2, help_text='Puede ser un numero entero o decimal. Máx 2 digitos decimales.')
	nombre_padre=models.CharField(max_length=512, verbose_name=u'Nombre del Padre, Madre o Encargado: ')
	profesion_padre=models.CharField(max_length=1024, verbose_name=u'Profesion u Oficio del Padre, Madre o Encargado: ', help_text='Indique a que se dedica su Padre, Madre o Encargado.')
	telefono_padre=models.CharField(max_length=8, verbose_name=u'Telefono del Padre, Madre o Encargado: ',  null = True, blank = True,default = None)
	asoc_campesina_padre=models.ForeignKey(AsocCampesina, verbose_name=u'Asociacion campesina del Padre, Madre o Encargado: ', null = True, blank = True,default = None, related_name='padre_asoc_campesina')
	nombre_madre=models.CharField(max_length=512, null = True, blank = True,default = None)
	profesion_madre=models.CharField(max_length=1024, verbose_name=u'Profesion madre', null = True, blank = True,default = None)
	telefono_madre=models.CharField(max_length=8, verbose_name=u'Telefono madre', null = True, blank = True,default = None)
	asoc_campesina_madre=models.ForeignKey(AsocCampesina, verbose_name=u'Asociacion campesina madre', null = True, blank = True,default = None, related_name='madre_asoc_campesina')
	correo_electronico=models.CharField(max_length=256, null = True, blank = True,default = None)
	tiene_hijos=models.BooleanField(default=False)
	posicion_familiar=models.IntegerField(verbose_name=u'¿Que numero de hijo es usted (segun el orden de nacimiento)?:', help_text='Especifique si es el primero (1), segundo (2), tercero (3) etc. hijo de su familia, segun orden de nacimiento. EJEMPLO: Si Usted nacio de primero coloque el numero 1.')
	observaciones=models.TextField(max_length=2024, null = True, blank = True,default = None)
	codigo_registro=models.CharField(max_length=512, null = True, blank = True,default = None)
	usuario_creador=models.ForeignKey(User, related_name='alu_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True, null = True, blank = True)
	usuario_modificador=models.ForeignKey(User, related_name='alu_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True, null = True, blank = True)
	estado = models.BooleanField(default=True)
	
	class Meta:
		db_table = 'alumnos_alumnos'

class PreMatricula(models.Model):
	persona=models.ForeignKey(Persona)
	campus=models.ForeignKey(Campus)
	periodo_clases=models.ForeignKey(PeriodoClase)
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_prematricula")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_prematricula_1")
	fecha_modificacion=models.DateField(auto_now=True)
	
	class Meta:
		db_table = 'alumnos_pre_matricula'

class Matricula(models.Model):
	alumno= models.ForeignKey(Alumnos)
	campus=models.ForeignKey(Campus)
	periodo_clase=models.ForeignKey(Periodo)
	codigo_registro=models.CharField(max_length=20)
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_matricula")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_matricula_1")
	fecha_modificacion=models.DateField(auto_now=True)
	edificio=models.ForeignKey(Edificios)
	carrera=models.ForeignKey(Carrera)
	dormitorio=models.ForeignKey(EstructuraEdificio)
	estado_matricula=models.BooleanField()
	tipo_condicion_matricula=models.ForeignKey(TiposCondicionesMatricula)
	pre_matricula=models.ForeignKey(PreMatricula)

	class Meta:
		db_table = 'alumnos_matricula'

class MatriculaClases(models.Model):
	matricula=models.ForeignKey(Matricula)
	asignatura_seccion=models.ForeignKey(AsignaturaSeccion)
	asignatura_extraordinaria=models.ForeignKey(Asignatura)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='mcla_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='mcla_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'alumnos_matricula_clases'

## 23/08 cindy
class PreMatriculaClases(models.Model):
	pre_matricula=models.ForeignKey(PreMatricula)
	asignaturas=models.ForeignKey(Asignatura, related_name='pmdsc_asignatura')
	observaciones=models.TextField()
	asignatura_extraordinaria=models.ForeignKey(Asignatura, related_name='pmdsc_asignatura_extra')
	usuario_creador=models.ForeignKey(User, related_name='pmc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='pmc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'alumnos_pre_matricula_clases'

#################### de registro alumnos
class Notas(models.Model):
	matricula_clase=models.ForeignKey(MatriculaClases)
	parcial=models.ForeignKey(Parcial)
	nota=models.DecimalField(max_digits=3, decimal_places=2)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='nota_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='nota_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'alumnos_notas'

class DocumentosAlumnos(models.Model):
	estado=models.IntegerField()
	observaciones=models.TextField()
	matricula=models.ForeignKey(Matricula)
	documento=models.ForeignKey(Documentos)
	usuario_creador=models.ForeignKey(User, related_name='da_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='da_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'alumnos_documentos_alumnos'

####################
class AlumnosBecas(models.Model):

	alumno = models.ForeignKey(Alumnos)
	matricula=models.ForeignKey(Matricula)
	tipo_beca=models.ForeignKey(TipoBeca)
	financiador=models.ForeignKey(Financiador)
	observacion=models.TextField()
	usuario_creador=models.ForeignKey(User,related_name="ab_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="ab_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)

	class Meta:
		db_table = 'alumnos_alumnos_becas'
	

class EstadoCuenta(models.Model):
	codigo_registro = models.CharField(max_length=15)
	descripcion= models.CharField(max_length=256)
	valor_matricula=models.IntegerField()
	valor_debe=models.DecimalField(max_digits=10, decimal_places=2)
	valor_haber=models.DecimalField(max_digits=10, decimal_places=2)
	alumnos_becas=models.ForeignKey(AlumnosBecas)
	usuario_creador=models.ForeignKey(User,related_name="ec_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="ec_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table = 'alumnos_estado_cuenta'


#Por Katherine
class Promocion(models.Model):
	alumno = models.ForeignKey(Alumnos)
	carrera=models.ForeignKey(Carrera)
	clase = models.IntegerField()
	periodo_academico = models.CharField(max_length=25) 
	usuario_creador=models.ForeignKey(User,related_name="promocion_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="promocion_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)






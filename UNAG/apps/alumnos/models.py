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

class alumnos(models.Model):
	persona=models.ForeignKey(persona)
	promedio_graduacion=models.DecimalField(max_digits=5, verbose_name='Promedio de graduación (Obtenido en diversificado)', decimal_places=2, help_text='Puede ser un número entero o decimal. Máx 2 digitos decimales.')
	nombre_padre=models.CharField(max_length=512, verbose_name='Nombre del Padre, Madre ó Encargado: ')
	profesion_padre=models.CharField(max_length=1024, verbose_name='Profesión u Oficio del Padre, Madre ó Encargado: ', help_text='Indique a qué se dedica su Padre, Madre ó Encargado.')
	telefono_padre=models.CharField(max_length=8, verbose_name='Teléfono del Padre, Madre ó Encargado: ', validators=[validar(tipo='telefono', longitud=8)], null = True, blank = True,default = None)
	asoc_campesina_padre=models.ForeignKey(asoc_campesina, verbose_name='Asociación campesina del Padre, Madre ó Encargado: ', null = True, blank = True,default = None, related_name='padre_asoc_campesina')
	nombre_madre=models.CharField(max_length=512, null = True, blank = True,default = None)
	profesion_madre=models.CharField(max_length=1024, verbose_name='Profesión madre', null = True, blank = True,default = None)
	telefono_madre=models.CharField(max_length=8, verbose_name='Teléfono madre', validators=[validar(tipo='telefono', longitud=8)], null = True, blank = True,default = None)
	asoc_campesina_madre=models.ForeignKey(asoc_campesina, verbose_name='Asociación campesina madre', null = True, blank = True,default = None, related_name='madre_asoc_campesina')
	correo_electronico=models.CharField(max_length=256, null = True, blank = True,default = None)
	tiene_hijos=models.BooleanField()
	posicion_familiar=models.IntegerField(verbose_name='¿Qué número de hijo es usted (según el orden de nacimiento)?:', help_text='Especifique si es el primero (1), segundo (2), tercero (3) etc. hijo de su familia, según orden de nacimiento. EJEMPLO: Si Usted nació de primero coloque el número 1.')
	observaciones=models.TextField(max_length=2024, null = True, blank = True,default = None)
	codigo_registro=models.CharField(max_length=512, null = True, blank = True,default = None)
	usuario_creador=models.ForeignKey(User, related_name='alu_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='alu_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

class pre_matricula(models.Model):
	persona=models.ForeignKey(persona)
	campus=models.ForeignKey(campus)
	periodo_clases=models.ForeignKey(periodo_clase)
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_prematricula")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_prematricula_1")
	fecha_modificacion=models.DateField(auto_now=True)

class matricula(models.Model):
	alumno= models.ForeignKey(alumnos)
	campus=models.ForeignKey(campus)
	periodo_clase=models.ForeignKey(periodo)
	codigo_registro=models.CharField(max_length=20)
	usuario_creador=models.ForeignKey(User,related_name="fk_usuario_matricula")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="fk_usuario_matricula_1")
	fecha_modificacion=models.DateField(auto_now=True)
	edificio=models.ForeignKey(edificios)
	carrera=models.ForeignKey(carrera)
	dormitorio=models.ForeignKey(estructura_edificio)
	estado_matricula=models.BooleanField()
	tipo_condicion_matricula=models.ForeignKey(tipos_condiciones_matricula)
	pre_matricula=models.ForeignKey(pre_matricula)

class matricula_clases(models.Model):
	matricula=models.ForeignKey(matricula)
	asignatura_seccion=models.ForeignKey(asignatura_seccion)
	asignatura_extraordinaria=models.ForeignKey(asignatura)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='mcla_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='mcla_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

## 23/08 cindy

class pre_matricula_clases(models.Model):
	pre_matricula=models.ForeignKey(pre_matricula)
	asignaturas=models.ForeignKey(asignatura, related_name='pmdsc_asignatura')
	observaciones=models.TextField()
	asignatura_extraordinaria=models.ForeignKey(asignatura, related_name='pmdsc_asignatura_extra')
	usuario_creador=models.ForeignKey(User, related_name='pmc_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='pmc_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
#################### de registro alumnos
class notas(models.Model):
	matricula_clase=models.ForeignKey(matricula_clases)
	parcial=models.ForeignKey(parcial)
	nota=models.DecimalField(max_digits=3, decimal_places=2)
	observaciones=models.TextField()
	usuario_creador=models.ForeignKey(User, related_name='nota_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='nota_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

class documentos_alumnos(models.Model):
	estado=models.IntegerField()
	observaciones=models.TextField()
	matricula=models.ForeignKey(matricula)
	documento=models.ForeignKey(documentos)
	usuario_creador=models.ForeignKey(User, related_name='da_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='da_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

####################
class alumnos_becas(models.Model):
	alumno = models.ForeignKey(alumnos)
	matricula=models.ForeignKey(matricula)
	tipo_beca=models.ForeignKey(tipo_beca)
	financiador=models.ForeignKey(financiador)
	observacion=models.TextField()
	usuario_creador=models.ForeignKey(User,related_name="ab_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="ab_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)
	
class estado_cuenta(models.Model):
	codigo_registro = models.CharField(max_length=15)
	descripcion= models.CharField(max_length=256)
	valor_matricula=models.IntegerField()
	valor_debe=models.DecimalField(max_digits=10, decimal_places=2)
	valor_haber=models.DecimalField(max_digits=10, decimal_places=2)
	alumnos_becas=models.ForeignKey(alumnos_becas)
	usuario_creador=models.ForeignKey(User,related_name="ec_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="ec_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)

class Promocion(models.Model):
	alumno = models.ForeignKey(alumnos)
	carrera=models.ForeignKey(carrera)
	clase = models.CharField(max_length=25)
	periodo_academico = models.IntegerField()
	usuario_creador=models.ForeignKey(User,related_name="promocion_usuario_creador")
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User,related_name="promocion_usuario_modificador")
	fecha_modificacion=models.DateField(auto_now=True)





# -*- encoding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from UNAG.apps.alumnos.models import *
from UNAG.apps.general.models import *
from django.forms import ModelForm, formsets, fields

class CampusForm(ModelForm):
	class Meta:
		model = campus
		exclude = ('usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	codigo=forms.CharField(max_length=32, label=u'Código',help_text='Este código puede estar compuesto por numeros y letras')
	descripcion = telefono = forms.CharField(max_length=128, label=u'Descripción', widget=forms.TextInput(attrs={'class': 'form-control'}))
	siglas = forms.CharField(max_length=15, label=u'Siglas', widget=forms.TextInput(attrs={'class': 'form-control'}))
	direccion = forms.CharField(max_length=128, label=u'Dirección', widget=forms.TextInput(attrs={'class': 'form-control'}))
	telefono = forms.CharField(max_length=9, label=u'Teléfono', help_text='Número de teléfono debe ingresarse sin guiones (-). Máx. 8 dígitos', widget=forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'}))
	director_campus = forms.ModelChoiceField(queryset = persona.objects.filter(tipo_persona__in = (5,7)),required=False, label=u'Rector/Director', widget=forms.Select(attrs={'class': 'chosen-select'}))

	def clean_descripcion(self):
		return self.cleaned_data["descripcion"].upper()


	
	#def upper(descripcion):	"""Converts a string into all uppercase."""
	#	return descripcion.upper()

class CampusEditForm(ModelForm):
	class Meta:
		model = campus
		exclude = ('usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	descripcion = telefono = forms.CharField(max_length=128, label=u'Descripción', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}))
	siglas = forms.CharField(max_length=15, label=u'Siglas', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}))
	direccion = forms.CharField(max_length=128, label=u'Dirección', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}))
	telefono = forms.CharField(max_length=9, label=u'Teléfono', widget=forms.TextInput(attrs={'placeholder':'########', 'class': 'form-control', 'disabled':'disabled'}))
	director_campus = forms.ModelChoiceField(queryset = persona.objects.filter(tipo_persona__in = (5,7)), required=False, label=u'Rector/Director', widget=forms.Select(attrs={'class': 'chosen-select', 'disabled':'disabled'}))



class EdificiosForm(ModelForm):
	class Meta:
		model = edificios
		exclude = ('usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	codigo=forms.CharField(label='Código')	
	ubicacion=forms.CharField(label='Ubicación')

# formularios administracion de PERSONAS

#form persona general	
class PersonaForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.all().distinct('descripcion'), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.all().distinct('descripcion'), label=u'Centros de Estudio')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.exclude(pk__in=[1,2,3,8,9,12]), label=u'Tipo persona', widget=forms.Select()) 


class PersonaEditForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')

#form persona alumno primer ingreso
class AspirantePersonaForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(descripcion__iexact='candidato'), label=u'Tipo persona', widget=forms.Select())

class AspirantePersonaEditForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(descripcion__iexact='candidato'), label=u'Tipo persona', widget=forms.Select())

#form persona alumno reingreso
class AlumnoPersonaForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(descripcion__iexact='estudiante reingreso'), label=u'Tipo persona', widget=forms.Select())
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.filter(grupo_grado__id=1), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[1,4]).distinct('descripcion'), label=u'Centros de Estudio')

class AlumnoPersonaEditForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(descripcion__iexact='estudiante reingreso'), label=u'Tipo persona', widget=forms.Select())
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.filter(grupo_grado__id=1), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[1,4]).distinct('descripcion'), label=u'Centros de Estudio')

#form persona docente
class DocentePersonaForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(pk__in=[3]), label=u'Tipo persona', widget=forms.Select())
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.exclude(grupo_grado__id=1).distinct('descripcion'), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[2]).distinct('descripcion'), label=u'Centros de Estudio')

class DocentePersonaEditForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.filter(pk__in=[3,8,9,12,5,6,7]), label=u'Tipo persona', widget=forms.Select())
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.exclude(grupo_grado__id=1).distinct('descripcion'), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[2]).distinct('descripcion'), label=u'Centros de Estudio')

#form persona docente
class DocenteAdministrativoForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.exclude(pk__in=[1,2,8,9,12,10,11,13,14]), label=u'Tipo persona', widget=forms.Select()) 
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.exclude(grupo_grado__id=1).distinct('descripcion'), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[2]).distinct('descripcion'), label=u'Centros de Estudio')

class DocenteAdministrativoEditForm(ModelForm):
	class Meta:
		model = persona
		exclude = ('aldea', 'caserio', 'barrio','telefono_fijo', 'fax', 'usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	tipo_persona = forms.ModelChoiceField(queryset = tipo_persona.objects.exclude(pk__in=[1,2,8,9,12,10,11,13,14]), label=u'Tipo persona', widget=forms.Select()) 
	titulos = forms.ModelMultipleChoiceField(queryset = titulos.objects.exclude(grupo_grado__id=1).distinct('descripcion'), label=u'Títulos')
	centros = forms.ModelMultipleChoiceField(queryset = centro.objects.filter(tipo_centro__id__in=[2]).distinct('descripcion'), label=u'Centros de Estudio')


# FIN

class CentroForm(ModelForm):
	class Meta:
		model = centro
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')


class DormitorioForm(ModelForm):
	class Meta:
		model = estructura_edificio
		exclude = ('usuario', 'usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	capacidad_personas=fields.IntegerField(validators=[RegexValidator("^[0-9]+$")], widget=forms.TextInput(attrs={'size':'3', 'maxlength':'3'}))
	codigo=forms.CharField(label='Código')
	descripcion=forms.CharField(label='Descripción')

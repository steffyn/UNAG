# -*- encoding: utf-8 -*-
from django import forms
from UNAG.apps.alumnos.models import *
from UNAG.apps.general.models import *
from UNAG.apps.registro.models import *
from django.forms import ModelForm, formsets, fields
from django.core.exceptions import ValidationError
from django.db import models
from django.forms.formsets import formset_factory
from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class MyCustomRenderer( RadioFieldRenderer ):
    def render( self ):
        """Outputs a series of <td></td> fields for this set of radio fields."""
        return(u'&nbsp;&nbsp;&nbsp;&nbsp;'.join( [ u'<td style="color: fff;">%s</td>' % force_unicode(w) for w in self ] ))

class DepartamentoAcademicoForm(ModelForm):
	class Meta:
		model = departamento_academico
		exclude = ('cod_usuario_creador', 'cod_usuario_modificador', 'fecha_modificacion')
	codigo=forms.CharField(max_length=28,label=u'Código',help_text='Este código puede estar compuesto por numeros y letras')
	descripcion = forms.CharField(max_length=128, label=u'Descripción', widget=forms.TextInput(attrs={'class': 'form-control'}))
	fecha_creacion = forms.DateField(label=u'Fecha de Creación', widget=forms.TextInput(attrs={'class': 'form-control'}))
	id_campus = forms.ModelChoiceField(queryset = campus.objects.all(), label=u'Campus', widget=forms.Select(attrs={'class': 'chosen-select'}))
	jefe=forms.ModelChoiceField(queryset = persona.objects.select_related('docente_departamento__persona').filter(docente_departamento__tipo_docente = 1), label=u'Jefe de Departamento', required=False)

class DepartamentoAcademicoEditForm(ModelForm):
	class Meta:
		model = departamento_academico
		exclude = ('cod_usuario_creador', 'cod_usuario_modificador', 'fecha_modificacion')
	codigo=forms.CharField(max_length=28, label=u'Código')
	descripcion = forms.CharField(max_length=128, label=u'Descripción', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}))
	fecha_creacion = forms.DateField(label=u'Fecha de Creación', widget=forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled' }))
	id_campus = forms.ModelChoiceField(queryset = campus.objects.all(), label=u'Campus', widget=forms.Select(attrs={'class': 'chosen-select' , 'disabled':'disabled'}))
	jefe=forms.ModelChoiceField(queryset = persona.objects.select_related('docente_departamento__persona').filter(docente_departamento__tipo_docente = 1), label=u'Jefe de Departamento')

class CarreraForm(ModelForm):
	Modalidad_CHOICES = (('INTERNADO', 'Internado'),('EXTERNADO', 'Externado'))
	class Meta:
		model = carrera
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
	codigo=forms.CharField(label=u'Código')	
	modalidad = forms.ChoiceField(choices= Modalidad_CHOICES, widget=forms.RadioSelect(renderer=MyCustomRenderer))
	cant_uv=forms.IntegerField(label=u'Cantidad Unidades Valorativas')
	cant_asignaturas=forms.IntegerField(label=u'Cantidad Asignaturas')
	cant_laboratorios=forms.IntegerField(label=u'Cantidad Laboratorios')
	uv_laboratorios=forms.IntegerField(label=u'Unidades Valorativas Laboratorios')
	uv_pps=forms.IntegerField(label=u'Unidades Valorativas PPS')
	persona_responsable = forms.ModelChoiceField(queryset = persona.objects.select_related('docente_departamento__persona').filter(docente_departamento__tipo_docente = 3), label=u'Coordinador de carrera')
	depto_academico=forms.ModelChoiceField(departamento_academico.objects, label=u'Departamento Academico')

class DocumentoForm(ModelForm):
	class Meta:
		model = documentos
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')

	cod_documento=forms.CharField(max_length=32,label=u'Código del Documento')
	descripcion=forms.CharField(label=u'Descripción')

class AsignaturaForm(ModelForm):
	class Meta:
		model = asignatura
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
	codigo_registro=forms.CharField(label=u'Código registro')

class DocenteForm(ModelForm):
	class Meta:
		model = docente_departamento
		exclude = ('persona', 'activo', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')

class TipoAsignaturaForm(ModelForm):
	class Meta:
		model = tipo_asignatura
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
	descripcion=forms.CharField(label=u'Descripción')	

class TipoCMForm(ModelForm):
	class Meta:
		model = tipos_condiciones_matricula
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')

class SeccionForm(ModelForm):
	class Meta:
		model = seccion
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
	#jornada=forms.ModelChoiceField(queryset = jornada.objects.all(), label=u'Jornada')
	#carrera=forms.ModelChoiceField(queryset = carrera.objects.all(), label=u'Carrera')
	periodo_clase=forms.ModelChoiceField(queryset = periodo_clase.objects.filter(habilitar_ingreso=True), label=u'Período Clase', initial=periodo_clase.objects.filter(habilitar_ingreso=True).values('id'))
	aula=forms.ModelChoiceField(queryset = estructura_edificio.objects.filter(edificio__tipo_edificio__descripcion__contains='Aula'), label=u'Aula')

class HorarioForm(ModelForm):
	class Meta:
		model = horario
		exclude = ('usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
	periodo_clase=forms.ModelChoiceField(queryset = periodo_clase.objects.filter(habilitar_ingreso=True), label=u'Período Clase', initial=periodo_clase.objects.filter(habilitar_ingreso=True).values('id'))

class HorarioHoraForm(ModelForm):
	class Meta:
		model = horario_hora
		exclude = ('horario', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')

	def validar(self, id_):
		error=True
		hi=  self.cleaned_data['hora_inicial']
		hf=  self.cleaned_data['hora_final']
		if(hf <= hi):
			error=False
			self._errors['hora_inicial']=self.error_class([u"La hora inicial debe ser mayor a la hora final."])
		else:
			for h in horario_hora.objects.filter(horario=horario.objects.get(pk=id_).id):
				if(hi >= h.hora_inicial and hi <= h.hora_final):
					error=False
					self._errors['hora_inicial']=self.error_class([u"Esta hora se traslapa con la hora "+str(h.hora_inicial)+"-"+str(h.hora_final)])
				elif(hf >= h.hora_inicial and hf <= h.hora_final):
					error=False
					self._errors['hora_inicial']=self.error_class([u"Esta hora se traslapa con la hora "+str(h.hora_inicial)+"-"+str(h.hora_final)])
				elif(hi <= h.hora_inicial and hf >= h.hora_final):
					error=False
					self._errors['hora_inicial']=self.error_class([u"Esta hora se traslapa con la hora "+str(h.hora_inicial)+"-"+str(h.hora_final)])
		return error

class AsignaturaSeccionForm(ModelForm):
	class Meta:
		model = asignatura_seccion
		exclude = ('horario_hora', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')


class RequisitoForm(ModelForm):
	class Meta:
		model = requisito
		exclude = ('asignatura_requisito','asignatura_base','usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'fecha_creacion')
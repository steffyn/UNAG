# -*- encoding: Latin-1 -*-
from django import forms
from UNAG.apps.alumnos.models import *
from UNAG.apps.general.models import *
from django.forms import ModelForm, formsets, fields
from django.utils.safestring import mark_safe
from UNAG.apps.general.models import archivos_guardados

#metodo para que los radio botones sean de forma horizontal
class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
        """Outputs radios"""
	return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class AlumnoForm(ModelForm):
	class Meta:
		model = Alumnos
		exclude = ('nombre_madre', 'profesion_madre', 'telefono_madre', 'telefono_madre', 'asoc_campesina_madre', 'persona','correo_electronico','codigo_registro','usuario_creador', 'fecha_creacion', 'usuario_modificador', 'fecha_modificacion')
	SiNo_CHOICES = ((True, 'Si'),(False, 'No'))
	tiene_hijos = forms.ChoiceField(label='¿Usted tiene hijos?:', widget=forms.RadioSelect(renderer=HorizRadioRenderer), required=True, choices=SiNo_CHOICES, initial=False)

class FormArchivosGuardados(forms.ModelForm):
	class Meta:
		model = archivos_guardados
		fields = '__all__'
		exclude = ['fecha_creacion', 'usuario_creador']
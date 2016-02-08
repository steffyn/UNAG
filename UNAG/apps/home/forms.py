#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

class FormLogin(forms.Form):
	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario', 'class': 'form-control'}))
	password = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'},render_value=False))

class excelForm(forms.Form):
	archivo=forms.FileField(label=u'Archivo CSV', help_text='<br><b>Archivo CSV, max. 1 MB, tipos de archivo permitidos csv</b>')


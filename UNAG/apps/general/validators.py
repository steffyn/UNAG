#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import mimetypes
from os.path import splitext

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat


class validar(object):

    def __init__(self, *args, **kwargs):
        self.tipo = kwargs.pop('tipo', None)
        self.longitud = kwargs.pop('longitud', None)
        self.min_size = kwargs.pop('min_size', 0)
        self.max_size = kwargs.pop('max_size', None)

    def __call__(self, value):
        if self.tipo == 'identidad' or self.tipo == 'telefono':
            if len(value) != self.longitud:
                raise ValidationError(u'%s tiene un formato inválido, mostrando %s caracteres' % (value, len(value)))
            if not value.isdigit():
                raise ValidationError(u'%s tiene un formato inválido, mostrando letras u otro caracter especial' % (value))

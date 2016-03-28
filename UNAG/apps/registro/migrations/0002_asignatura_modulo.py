# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='modulo',
            field=models.ManyToManyField(related_name='modulo_rel_+', to='registro.Asignatura'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_asignatura_modulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='modulo',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='docente_carrera',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='periodo_clase',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='tipo_asignatura',
        ),
        migrations.AddField(
            model_name='modulo',
            name='carrera',
            field=models.ForeignKey(default=9, to='registro.Carrera'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='laboratorio',
            field=models.ForeignKey(related_name='laboratorio_id', default=34, verbose_name=b'laboratorios', to='registro.Asignatura', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='modulo',
            field=models.ForeignKey(related_name='modulo_id', default=36, to='registro.Asignatura'),
            preserve_default=False,
        ),
    ]

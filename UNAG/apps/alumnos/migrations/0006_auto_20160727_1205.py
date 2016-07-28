# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_alumnos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='telefono_encargado',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono Encargado', blank=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='asoc_campesina_padre',
            field=models.ForeignKey(related_name='padre_asoc_campesina', default=None, blank=True, to='general.AsocCampesina', null=True, verbose_name='Asociacion campesina del Padre: '),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombre_padre',
            field=models.CharField(max_length=512, verbose_name='Nombre del Padre: '),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='profesion_padre',
            field=models.CharField(help_text=b'Indique a que se dedica su Padre, Madre o Encargado.', max_length=1024, verbose_name='Profesion u Oficio del Padre:'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='telefono_padre',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono del Padre: ', blank=True),
        ),
    ]

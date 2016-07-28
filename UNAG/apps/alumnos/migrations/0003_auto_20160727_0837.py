# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alumnos_identidad_padre'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='antiguo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='beca',
            field=models.IntegerField(default=0, verbose_name='Beca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='identidad_encargado',
            field=models.CharField(default='', max_length=18, verbose_name='Identidad Encargado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='identidad_madre',
            field=models.CharField(default='', max_length=18, verbose_name='Identidad Madre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='ingreso_mensual_familiar',
            field=models.DecimalField(default=0, verbose_name='Ingreso mensual Familiar', max_digits=18, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='nombre_encargado',
            field=models.CharField(default='', max_length=512, verbose_name='Nombre del Encargado: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='otros_padecimientos',
            field=models.TextField(default=None, max_length=2024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='personas_en_casa',
            field=models.IntegerField(default=0, verbose_name='\xbfCuantas personas viven en su casa?:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='profesion_encargado',
            field=models.CharField(default='', help_text=b'Indique a que se dedica su Encargado.', max_length=1024, verbose_name='Profesion u Oficio del Encargado: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='religion',
            field=models.CharField(default='', max_length=256, verbose_name='Nombre del Padre, Madre o Encargado: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='trabaja',
            field=models.BooleanField(default=False),
        ),
    ]

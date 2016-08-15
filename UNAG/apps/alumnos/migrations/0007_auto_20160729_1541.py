# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumnos', '0006_auto_20160727_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='bc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='bc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Etnias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='et_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='et_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='asoc_campesina_madre',
            field=models.ForeignKey(related_name='madre_asoc_campesina', default=None, blank=True, to='general.AsocCampesina', null=True, verbose_name='Asociacion campesina'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='asoc_campesina_padre',
            field=models.ForeignKey(related_name='padre_asoc_campesina', default=None, blank=True, to='general.AsocCampesina', null=True, verbose_name='Asociacion campesina'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='beca',
            field=models.ForeignKey(related_name='alu_beca', to='alumnos.Becas'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='identidad_encargado',
            field=models.CharField(max_length=18, verbose_name='Identidad'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='identidad_madre',
            field=models.CharField(max_length=18, verbose_name='Identidad'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='identidad_padre',
            field=models.CharField(max_length=18, verbose_name='Identidad'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombre_encargado',
            field=models.CharField(max_length=512, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombre_padre',
            field=models.CharField(max_length=512, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='personas_en_casa',
            field=models.IntegerField(verbose_name='\xbfCuantas personas viven en su casa?'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='posicion_familiar',
            field=models.IntegerField(help_text=b'Especifique si es el primero (1), segundo (2), tercero (3) etc. hijo de su familia, segun orden de nacimiento. EJEMPLO: Si Usted nacio de primero coloque el numero 1.', verbose_name='\xbfQue numero de hijo es usted (segun el orden de nacimiento)?'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='profesion_encargado',
            field=models.CharField(help_text=b'Indique a que se dedica su Encargado.', max_length=1024, verbose_name='Profesion u Oficio'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='profesion_madre',
            field=models.CharField(default=None, max_length=1024, null=True, verbose_name='Profesion u Oficio', blank=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='profesion_padre',
            field=models.CharField(help_text=b'Indique a que se dedica su Padre, Madre o Encargado.', max_length=1024, verbose_name='Profesion u Oficio'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='religion',
            field=models.CharField(max_length=256, verbose_name='Religi\xf3n a la que pertenece'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='telefono_encargado',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono', blank=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='telefono_madre',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono', blank=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='telefono_padre',
            field=models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono', blank=True),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='etnia',
            field=models.ForeignKey(blank=True, to='alumnos.Etnias', null=True),
        ),
    ]

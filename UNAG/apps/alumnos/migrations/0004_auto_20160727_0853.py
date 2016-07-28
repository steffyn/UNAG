# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumnos', '0003_auto_20160727_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='id_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='id_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Padecimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='pd_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='pd_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alumnos',
            name='idiomas',
            field=models.ManyToManyField(to='alumnos.Idiomas', verbose_name=b'Idiomas'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='padecimientos',
            field=models.ManyToManyField(to='alumnos.Padecimientos', verbose_name=b'Padecimientos'),
        ),
    ]

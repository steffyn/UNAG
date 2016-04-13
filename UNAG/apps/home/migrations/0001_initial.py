# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
<<<<<<< HEAD
=======
import django.contrib.auth.models
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('auth', '0001_initial'),
=======
        ('auth', '0006_require_contenttypes_0002'),
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'home_rol',
                'permissions': (('can_view_menu', 'Puede ver el menu de registro'), ('can_view_home_censo', 'Puede ver pantalla inicio censo'), ('can_view_menu_registro', 'Puede ver el menu de registro'), ('can_recuperar_clave', 'Puede recuperar clave de usuarios'), ('can_view_avance_censo', 'Puede ver el avance del censo'), ('can_view_menu_censo', 'Puede ver el menu del censo')),
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'home_tipo_usuario',
            },
<<<<<<< HEAD
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
=======
        ),
        migrations.CreateModel(
            name='User',
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('codigo_registro', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('telefono', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('direccion', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('tipo_usuario', models.ForeignKey(default=None, blank=True, to='home.TipoUsuario', null=True)),
            ],
            options={
                'db_table': 'home_user',
            },
            bases=('auth.user',),
<<<<<<< HEAD
=======
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='usuario_creador',
            field=models.ForeignKey(related_name='tu_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='tu_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='rol',
            name='usuario_creador',
            field=models.ForeignKey(related_name='rol_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='rol',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='rol_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
    ]

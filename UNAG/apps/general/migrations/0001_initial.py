# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import UNAG.apps.general.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aldea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'general_aldea',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='archivos_guardados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=UNAG.apps.general.models.url)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
<<<<<<< HEAD
            options={
            },
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='AsocCampesina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=1024)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='ac_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ac_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_asoc_campesina',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'general_barrio',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=32)),
                ('descripcion', models.CharField(max_length=128)),
                ('siglas', models.CharField(unique=True, max_length=32)),
                ('direccion', models.CharField(max_length=256)),
                ('telefono', models.CharField(help_text=b'N\xc3\xbamero de tel\xc3\xa9fono sin guiones (-)', max_length=8)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'general_campus',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Caserio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('aldea', models.ForeignKey(to='general.Aldea')),
                ('usuario_creador', models.ForeignKey(related_name='cas_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='cas_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_caserio',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=1024)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'general_centro',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_departamento', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=64)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='dep_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='dep_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_departamento',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Edificios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=32)),
                ('nombre', models.CharField(max_length=256)),
                ('ubicacion', models.CharField(max_length=512)),
                ('capacidad_total_personas', models.IntegerField()),
                ('cantidad_dormitorios', models.IntegerField(help_text=b'Especifique la cantidad de aulas, dormitorios, oficinas, laboratorios..., seg\xc3\xban el tipo de edificio seleccionado.', verbose_name=b'Cantidad de espacios f\xc3\xadsicos')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('campus', models.ForeignKey(to='general.Campus')),
            ],
            options={
                'db_table': 'general_edificios',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='ecs_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ecs_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_estado_civil',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='EstructuraEdificio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=13)),
                ('descripcion', models.CharField(unique=True, max_length=512)),
                ('capacidad_personas', models.IntegerField()),
                ('ocupados', models.IntegerField(default=None, null=True, verbose_name=b'Cantidad ocupados', blank=True)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('edificio', models.ForeignKey(to='general.Edificios')),
                ('usuario_creador', models.ForeignKey(related_name='fk_usuario_carrera', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='fk_usuario_carrera_1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_estructura_edificio',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Financiador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_financiador', models.CharField(max_length=1024)),
                ('direccion', models.CharField(max_length=1024)),
                ('telefono', models.CharField(max_length=20)),
                ('nombre_contacto', models.CharField(max_length=256)),
                ('correo_electronico', models.CharField(max_length=256)),
                ('observaciones', models.TextField(max_length=2024)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='fin_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='fin_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_financiador',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='GrupoGrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_grupo_grado',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='jor_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='jor_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_jornada',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Modalidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='moda_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='moda_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_modalidades',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_municipio', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=64)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('departamento', models.ForeignKey(to='general.Departamento')),
                ('usuario_creador', models.ForeignKey(related_name='mun_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='mun_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_municipio',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='pais_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='pais_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_pais',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('clase', models.IntegerField()),
                ('descripcion', models.CharField(max_length=65)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
=======
                ('descripcion', models.CharField(max_length=65)),
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='pr_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='pr_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_periodo',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='PeriodoClase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('descripcion', models.CharField(max_length=128, verbose_name=b'Periodo Academico')),
=======
                ('descripcion', models.CharField(max_length=128)),
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('periodo', models.ForeignKey(to='general.Periodo')),
                ('usuario_creador', models.ForeignKey(related_name='pc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='pc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_periodo_clase',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identidad', models.CharField(unique=True, max_length=18)),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('genero', models.CharField(max_length=2, verbose_name=b'G\xc3\xa9nero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.CharField(max_length=2024, verbose_name=b'Direcci\xc3\xb3n')),
                ('correo_electronico', models.EmailField(help_text=b'Indique un correo electr\xc3\xb3nico v\xc3\xa1lido. Formato correo@dominio.com', unique=True, max_length=256, verbose_name=b'Correo electr\xc3\xb3nico')),
                ('celular', models.CharField(help_text='Ingrese el n\xfamero sin guiones (-)', max_length=8)),
                ('telefono_fijo', models.CharField(default=None, max_length=8, blank=True, help_text='Ingrese el n\xfamero sin guiones (-)', null=True, verbose_name=b'Tel\xc3\xa9fono fijo')),
                ('fax', models.CharField(default=None, max_length=18, null=True, blank=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('aldea', models.ForeignKey(default=None, blank=True, to='general.Aldea', null=True)),
                ('barrio', models.ForeignKey(default=None, blank=True, to='general.Barrio', null=True)),
                ('caserio', models.ForeignKey(default=None, blank=True, to='general.Caserio', null=True, verbose_name=b'Caser\xc3\xado')),
                ('centros', models.ManyToManyField(to='general.Centro', verbose_name=b'Centros de Estudio')),
                ('departamento', models.ForeignKey(default=None, blank=True, to='general.Departamento', null=True)),
                ('estado_civil', models.ForeignKey(to='general.EstadoCivil')),
                ('municipio', models.ForeignKey(default=None, blank=True, to='general.Municipio', null=True)),
                ('pais_nacimiento', models.ForeignKey(related_name='nac_pais_nacimiento', to='general.Pais')),
                ('pais_residencia', models.ForeignKey(related_name='res_pais_residencia', to='general.Pais')),
            ],
            options={
                'db_table': 'general_persona',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoAdministracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='ta_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ta_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_adinistracion',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoBeca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='tb_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tb_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_beca',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoCentro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=1024)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('tipo_administracion', models.ForeignKey(to='general.TipoAdministracion')),
                ('usuario_creador', models.ForeignKey(related_name='tc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_centro',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoEdificios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='tedi_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tedi_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_edificios',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='td_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='td_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_identificacion',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='tp_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tp_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_tipo_persona',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Titulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('grupo_grado', models.ForeignKey(to='general.GrupoGrado')),
                ('usuario_creador', models.ForeignKey(related_name='ti_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ti_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_titulos',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='zona_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='zona_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_zona',
            },
<<<<<<< HEAD
            bases=(models.Model,),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.ForeignKey(verbose_name=b'Tipo de identificaci\xc3\xb3n', to='general.TipoIdentificacion'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_persona',
            field=models.ForeignKey(to='general.TipoPersona'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='titulos',
            field=models.ManyToManyField(help_text='Seleccione en el lado derecho los t\xedtulos que desea agregar pulsando el boton (+),  ', to='general.Titulos', verbose_name=b'T\xc3\xadtulos Obtenidos'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.OneToOneField(related_name='person_usuario_posee', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario_creador',
            field=models.ForeignKey(related_name='per_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='per_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='persona',
            name='zona',
            field=models.ForeignKey(to='general.Zona'),
<<<<<<< HEAD
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='estructuraedificio',
            unique_together=set([('codigo', 'edificio')]),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='edificios',
            name='tipo_edificio',
            field=models.ForeignKey(to='general.TipoEdificios'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='edificios',
            name='usuario_creador',
            field=models.ForeignKey(related_name='edi_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='edificios',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='edi_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='edificios',
            unique_together=set([('codigo', 'campus')]),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='centro',
            name='tipo_centro',
            field=models.ForeignKey(to='general.TipoCentro'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='centro',
            name='usuario_creador',
            field=models.ForeignKey(related_name='ce_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='centro',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='ce_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='centro',
            name='zona',
            field=models.ForeignKey(to='general.Zona'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='campus',
            name='director_campus',
            field=models.OneToOneField(null=True, default=None, error_messages={b'unique': 'Este Director ya esta asignado a otro Campus.'}, to='general.Persona', blank=True),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='campus',
            name='usuario_creador',
            field=models.ForeignKey(related_name='cam_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='campus',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='cam_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='campus',
            unique_together=set([('codigo', 'siglas')]),
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='barrio',
            name='caserio',
            field=models.ForeignKey(to='general.Caserio'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='barrio',
            name='usuario_creador',
            field=models.ForeignKey(related_name='bo_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='barrio',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='bo_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='aldea',
            name='municipio',
            field=models.ForeignKey(to='general.Municipio'),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='aldea',
            name='usuario_creador',
            field=models.ForeignKey(related_name='al_usuario_creador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
        migrations.AddField(
            model_name='aldea',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='al_usuario_modificador', to=settings.AUTH_USER_MODEL),
<<<<<<< HEAD
            preserve_default=True,
=======
        ),
        migrations.AlterUniqueTogether(
            name='estructuraedificio',
            unique_together=set([('codigo', 'edificio')]),
        ),
        migrations.AlterUniqueTogether(
            name='edificios',
            unique_together=set([('codigo', 'campus')]),
        ),
        migrations.AlterUniqueTogether(
            name='campus',
            unique_together=set([('codigo', 'siglas')]),
>>>>>>> c93a59176b8e24468f92470aa03511bf667e7f44
        ),
    ]

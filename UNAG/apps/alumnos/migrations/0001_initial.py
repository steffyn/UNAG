# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promedio_graduacion', models.DecimalField(help_text=b'Puede ser un numero entero o decimal. M\xc3\xa1x 2 digitos decimales.', verbose_name='Promedio de graduacion (Obtenido en diversificado)', max_digits=5, decimal_places=2)),
                ('nombre_padre', models.CharField(max_length=512, verbose_name='Nombre del Padre, Madre o Encargado: ')),
                ('profesion_padre', models.CharField(help_text=b'Indique a que se dedica su Padre, Madre o Encargado.', max_length=1024, verbose_name='Profesion u Oficio del Padre, Madre o Encargado: ')),
                ('telefono_padre', models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono del Padre, Madre o Encargado: ', blank=True)),
                ('nombre_madre', models.CharField(default=None, max_length=512, null=True, blank=True)),
                ('profesion_madre', models.CharField(default=None, max_length=1024, null=True, verbose_name='Profesion madre', blank=True)),
                ('telefono_madre', models.CharField(default=None, max_length=8, null=True, verbose_name='Telefono madre', blank=True)),
                ('correo_electronico', models.CharField(default=None, max_length=256, null=True, blank=True)),
                ('tiene_hijos', models.BooleanField(default=False)),
                ('posicion_familiar', models.IntegerField(help_text=b'Especifique si es el primero (1), segundo (2), tercero (3) etc. hijo de su familia, segun orden de nacimiento. EJEMPLO: Si Usted nacio de primero coloque el numero 1.', verbose_name='\xbfQue numero de hijo es usted (segun el orden de nacimiento)?:')),
                ('observaciones', models.TextField(default=None, max_length=2024, null=True, blank=True)),
                ('codigo_registro', models.CharField(default=None, max_length=512, null=True, blank=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True)),
                ('asoc_campesina_madre', models.ForeignKey(related_name='madre_asoc_campesina', default=None, blank=True, to='general.AsocCampesina', null=True, verbose_name='Asociacion campesina madre')),
                ('asoc_campesina_padre', models.ForeignKey(related_name='padre_asoc_campesina', default=None, blank=True, to='general.AsocCampesina', null=True, verbose_name='Asociacion campesina del Padre, Madre o Encargado: ')),
                ('persona', models.ForeignKey(to='general.Persona')),
                ('usuario_creador', models.ForeignKey(related_name='alu_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='alu_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_alumnos',
            },
        ),
        migrations.CreateModel(
            name='AlumnosBecas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumnos')),
                ('financiador', models.ForeignKey(to='general.Financiador')),
            ],
            options={
                'db_table': 'alumnos_alumnos_becas',
            },
        ),
        migrations.CreateModel(
            name='DocumentosAlumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('documento', models.ForeignKey(to='registro.Documentos')),
            ],
            options={
                'db_table': 'alumnos_documentos_alumnos',
            },
        ),
        migrations.CreateModel(
            name='EstadoCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_registro', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=256)),
                ('valor_matricula', models.IntegerField()),
                ('valor_debe', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_haber', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('alumnos_becas', models.ForeignKey(to='alumnos.AlumnosBecas')),
                ('usuario_creador', models.ForeignKey(related_name='ec_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ec_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_estado_cuenta',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_registro', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('estado_matricula', models.BooleanField()),
                ('alumno', models.ForeignKey(to='alumnos.Alumnos')),
                ('campus', models.ForeignKey(to='general.Campus')),
                ('carrera', models.ForeignKey(to='registro.Carrera')),
                ('dormitorio', models.ForeignKey(to='general.EstructuraEdificio')),
                ('edificio', models.ForeignKey(to='general.Edificios')),
                ('periodo_clase', models.ForeignKey(to='general.Periodo')),
            ],
            options={
                'db_table': 'alumnos_matricula',
            },
        ),
        migrations.CreateModel(
            name='MatriculaClases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('asignatura_extraordinaria', models.ForeignKey(to='registro.Asignatura')),
                ('asignatura_seccion', models.ForeignKey(to='registro.AsignaturaSeccion')),
                ('matricula', models.ForeignKey(to='alumnos.Matricula')),
                ('usuario_creador', models.ForeignKey(related_name='mcla_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='mcla_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_matricula_clases',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.DecimalField(max_digits=3, decimal_places=2)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('matricula_clase', models.ForeignKey(to='alumnos.MatriculaClases')),
                ('parcial', models.ForeignKey(to='registro.Parcial')),
                ('usuario_creador', models.ForeignKey(related_name='nota_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='nota_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_notas',
            },
        ),
        migrations.CreateModel(
            name='PreMatricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('campus', models.ForeignKey(to='general.Campus')),
                ('periodo_clases', models.ForeignKey(to='general.PeriodoClase')),
                ('persona', models.ForeignKey(to='general.Persona')),
                ('usuario_creador', models.ForeignKey(related_name='fk_usuario_prematricula', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='fk_usuario_prematricula_1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_pre_matricula',
            },
        ),
        migrations.CreateModel(
            name='PreMatriculaClases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('asignatura_extraordinaria', models.ForeignKey(related_name='pmdsc_asignatura_extra', to='registro.Asignatura')),
                ('asignaturas', models.ForeignKey(related_name='pmdsc_asignatura', to='registro.Asignatura')),
                ('pre_matricula', models.ForeignKey(to='alumnos.PreMatricula')),
                ('usuario_creador', models.ForeignKey(related_name='pmc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='pmc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumnos_pre_matricula_clases',
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase', models.IntegerField()),
                ('periodo_academico', models.CharField(max_length=25)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumnos')),
                ('carrera', models.ForeignKey(to='registro.Carrera')),
                ('usuario_creador', models.ForeignKey(related_name='promocion_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='promocion_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='pre_matricula',
            field=models.ForeignKey(to='alumnos.PreMatricula'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='tipo_condicion_matricula',
            field=models.ForeignKey(to='registro.TiposCondicionesMatricula'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='usuario_creador',
            field=models.ForeignKey(related_name='fk_usuario_matricula', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matricula',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='fk_usuario_matricula_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentosalumnos',
            name='matricula',
            field=models.ForeignKey(to='alumnos.Matricula'),
        ),
        migrations.AddField(
            model_name='documentosalumnos',
            name='usuario_creador',
            field=models.ForeignKey(related_name='da_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentosalumnos',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='da_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alumnosbecas',
            name='matricula',
            field=models.ForeignKey(to='alumnos.Matricula'),
        ),
        migrations.AddField(
            model_name='alumnosbecas',
            name='tipo_beca',
            field=models.ForeignKey(to='general.TipoBeca'),
        ),
        migrations.AddField(
            model_name='alumnosbecas',
            name='usuario_creador',
            field=models.ForeignKey(related_name='ab_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alumnosbecas',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='ab_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
    ]

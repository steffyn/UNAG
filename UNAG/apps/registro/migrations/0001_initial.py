# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_registro', models.CharField(unique=True, max_length=512)),
                ('nombre_asignatura', models.CharField(max_length=1024)),
                ('uv', models.IntegerField(verbose_name=b'Unidades valorativas')),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'registro_asignatura',
            },
        ),
        migrations.CreateModel(
            name='AsignaturaBloque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bloque', models.CharField(max_length=1024)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('asignatura', models.ForeignKey(to='registro.Asignatura')),
                ('usuario_creador', models.ForeignKey(related_name='ablo_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='ablo_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_asignatura',
            },
        ),
        migrations.CreateModel(
            name='AsignaturaSeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=3, choices=[(b'Lun', b'Lunes'), (b'Mar', b'Martes'), (b'Mie', b'Miercoles'), (b'Jue', b'Jueves'), (b'Vie', b'Viernes'), (b'Sab', b'Sabado'), (b'Dom', b'Domingo')])),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('asignatura', models.ForeignKey(to='registro.Asignatura')),
            ],
            options={
                'db_table': 'registro_asignatura_seccion',
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=32, verbose_name=b'C\xc3\xb3digo')),
                ('nombre_carrera', models.CharField(max_length=256)),
                ('siglas_carrera', models.CharField(max_length=15)),
                ('duracion', models.DecimalField(help_text=b'Ingrese la duraci\xc3\xb3n en a\xc3\xb1os. Ej. Si una carrera dura 4 a\xc3\xb1os y medio ingrese 4.5', verbose_name=b'Duraci\xc3\xb3n', max_digits=4, decimal_places=2)),
                ('modalidad', models.CharField(max_length=30, verbose_name=b'Modalidad', choices=[(b'INTERNADO', b'Internado'), (b'EXTERNADO', b'Externado')])),
                ('fecha_aprobacion', models.DateField(verbose_name=b'Fecha de aprobaci\xc3\xb3n')),
                ('cant_uv', models.IntegerField()),
                ('cant_asignaturas', models.IntegerField()),
                ('cant_laboratorios', models.IntegerField()),
                ('uv_laboratorios', models.IntegerField()),
                ('uv_pps', models.IntegerField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('observaciones', models.TextField(max_length=1024)),
                ('campus', models.ForeignKey(to='general.Campus')),
            ],
            options={
                'db_table': 'registro_carrera',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=28)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('cod_usuario_creador', models.ForeignKey(related_name='fk_usuario_deptoa', to=settings.AUTH_USER_MODEL)),
                ('cod_usuario_modificador', models.ForeignKey(related_name='fk_usuario_deptoa_1', to=settings.AUTH_USER_MODEL)),
                ('id_campus', models.ForeignKey(to='general.Campus')),
                ('jefe', models.ForeignKey(default=None, blank=True, to='general.Persona', null=True)),
            ],
            options={
                'db_table': 'registro_departamento_academico',
            },
        ),
        migrations.CreateModel(
            name='docente_departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio_laboral', models.DateField(auto_now_add=True, verbose_name=b'Fecha en que inici\xc3\xb3 a laborar')),
                ('activo', models.BooleanField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('campus', models.ForeignKey(to='general.Campus')),
                ('departamento_academico', models.ForeignKey(verbose_name=b'Departamento acad\xc3\xa9mico al que pertenece', to='registro.DepartamentoAcademico')),
                ('jornada', models.ManyToManyField(to='general.Jornada')),
            ],
            options={
                'db_table': 'registro_docente_departamento',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_documento', models.CharField(help_text=b'Ingrese un c\xc3\xb3digo que identifique el documento', unique=True, max_length=32, error_messages={b'unique': 'Ya existe un Documento con este C\xf3digo.'})),
                ('descripcion', models.CharField(max_length=1024)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='doc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='doc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_documentos',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'registro_horario',
            },
        ),
        migrations.CreateModel(
            name='HorarioHora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_inicial', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('horario', models.ForeignKey(to='registro.Horario')),
                ('usuario_creador', models.ForeignKey(related_name='hhor_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='hhor_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_horario_hora',
            },
        ),
        migrations.CreateModel(
            name='JornadaLaboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='jlab_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='jlab_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_jornada_laboral',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'registro_modulo',
            },
        ),
        migrations.CreateModel(
            name='Parcial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('periodo_clase', models.ForeignKey(to='general.PeriodoClase')),
                ('usuario_creador', models.ForeignKey(related_name='parc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='parc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_parcial',
            },
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('asignatura_base', models.ForeignKey(related_name='req_asignatura_base', to='registro.Asignatura')),
                ('asignatura_requisito', models.ForeignKey(related_name='req_asignatura_requisito', to='registro.Asignatura')),
                ('usuario_creador', models.ForeignKey(related_name='req_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='req_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_requisito',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('aula', models.ForeignKey(to='general.EstructuraEdificio')),
                ('carrera', models.ForeignKey(to='registro.Carrera')),
                ('jornada', models.ForeignKey(to='general.Jornada')),
                ('periodo_clase', models.ForeignKey(to='general.PeriodoClase')),
                ('usuario_creador', models.ForeignKey(related_name='sec_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='sec_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_seccion',
            },
        ),
        migrations.CreateModel(
            name='TipoAsignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=512)),
                ('nota_aprobatorio', models.DecimalField(max_digits=4, decimal_places=0)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='tasi_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tasi_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_tipo_asignatura',
            },
        ),
        migrations.CreateModel(
            name='TipoDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=512)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='tdoc_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='tdoc_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_tipo_docente',
            },
        ),
        migrations.CreateModel(
            name='TiposCondicionesMatricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=1024)),
                ('acciones_condicion', models.CharField(max_length=2048)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creador', models.ForeignKey(related_name='cm_usuario_creador', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificador', models.ForeignKey(related_name='cm_usuario_modificador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registro_tipo_condiciones_matricula',
            },
        ),
        migrations.AddField(
            model_name='modulo',
            name='usuario_creador',
            field=models.ForeignKey(related_name='mod_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='modulo',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='mod_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='horario',
            name='seccion',
            field=models.ForeignKey(to='registro.Seccion'),
        ),
        migrations.AddField(
            model_name='horario',
            name='usuario_creador',
            field=models.ForeignKey(related_name='fk_usuario_horario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='horario',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='fk_usuario_horario_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docente_departamento',
            name='jornada_laboral',
            field=models.ForeignKey(to='registro.JornadaLaboral'),
        ),
        migrations.AddField(
            model_name='docente_departamento',
            name='persona',
            field=models.ForeignKey(to='general.Persona'),
        ),
        migrations.AddField(
            model_name='docente_departamento',
            name='tipo_docente',
            field=models.ForeignKey(to='registro.TipoDocente'),
        ),
        migrations.AddField(
            model_name='docente_departamento',
            name='usuario_creador',
            field=models.ForeignKey(related_name='ddep_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docente_departamento',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='ddep_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carrera',
            name='depto_academico',
            field=models.ForeignKey(to='registro.DepartamentoAcademico'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='grado',
            field=models.ForeignKey(to='general.GrupoGrado'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='persona_responsable',
            field=models.ForeignKey(to='general.Persona'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='usuario_creador',
            field=models.ForeignKey(related_name='fk_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carrera',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='fk_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignaturaseccion',
            name='docente_carrera',
            field=models.ForeignKey(verbose_name=b'Docente', to='registro.docente_departamento'),
        ),
        migrations.AddField(
            model_name='asignaturaseccion',
            name='horario_hora',
            field=models.ForeignKey(to='registro.HorarioHora'),
        ),
        migrations.AddField(
            model_name='asignaturaseccion',
            name='usuario_creador',
            field=models.ForeignKey(related_name='asec_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignaturaseccion',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='asec_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='carrera',
            field=models.ForeignKey(verbose_name=b'Carrera', to='registro.Carrera'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='tipo_asignatura',
            field=models.ForeignKey(related_name='tasi_asi_tipo_asignatura', to='registro.TipoAsignatura'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='usuario_creador',
            field=models.ForeignKey(related_name='asig_usuario_creador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='usuario_modificador',
            field=models.ForeignKey(related_name='asig_usuario_modificador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='seccion',
            unique_together=set([('jornada', 'carrera', 'periodo_clase', 'aula')]),
        ),
        migrations.AlterUniqueTogether(
            name='departamentoacademico',
            unique_together=set([('codigo', 'id_campus')]),
        ),
        migrations.AlterUniqueTogether(
            name='carrera',
            unique_together=set([('codigo', 'campus')]),
        ),
        migrations.AlterUniqueTogether(
            name='asignatura',
            unique_together=set([('codigo_registro', 'nombre_asignatura')]),
        ),
        migrations.AddField(
            model_name='modulo',
            name='carrera',
            field=models.ForeignKey(default=1, to='registro.Carrera'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='laboratorio',
            field=models.ForeignKey(related_name='laboratorio_id', default=1, verbose_name=b'laboratorios', to='registro.Asignatura', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulo',
            name='modulo',
            field=models.ForeignKey(related_name='modulo_id', default=1, to='registro.Asignatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignaturabloque',
            name='bloque',
            field=models.ForeignKey(default=1, to='registro.CarreraBloque'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='asignaturabloque',
            table='registro_asignatura_bloque',
        ),
    ]

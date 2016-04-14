from django.conf.urls import patterns, url

urlpatterns = patterns('UNAG.apps.alumnos.views',
	url(r'^student/view_new_student/$', 'new_student_view', name='vista_nuevo_estudiante'), #nuevas solicitudes	
	url(r'^student/view_profile_student/$', 'profile_student_view', name='vista_perfil_estudiante'),

	#urls menu administracion persona alumno
	url(r'^alumno/$', 'view_index_alumno', name='vista_index_alumno'),
	url(r'^censo/view_add_people_alu/$', 'view_add_people_alu', name='vista_nuevo_primer_ingreso'),
	url(r'^censo/reingreso/add/$', 'view_add_alumno_rein', name='vista_nuevo_reingreso'),
	url(r'^reingreso/login/$', 'view_login_reingreso', name='vista_login_reingreso'),
	url(r'^censo/personaalumno/edit/$', 'view_persona_alumno_edit', name='vista_persona_alumno_detalle'),
	url(r'^censo/alumnoreingreso/edit/$', 'view_senso_alumno_edit', name='vista_senso_alumno_detalle'),
	

	#por Katherine
	url(r'^registro/excel/$', 'alumnos_registro_excel', name='alumnos_registro_excel'),
	url(r'^registro/$', 'alumnos_registro', name='alumnos_registro'),
	url(r'^lista/$', 'alumnos_lista', name='alumnos_lista'),
	url(r'^editar/(?P<id>\d+)/$', 'alumnos_editar', name='alumnos_editar'),
	url(r'^eliminar/(?P<id>\d+)/$', 'alumnos_eliminar', name='alumnos_eliminar'),
)


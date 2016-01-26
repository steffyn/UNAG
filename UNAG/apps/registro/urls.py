from django.conf.urls import patterns, url

urlpatterns = patterns('UNAG.apps.registro.views',

	#urls index docente
	url(r'^docente/$', 'view_index_docente', name='vista_index_docente'),
	url(r'^docente/login/$', 'view_login_docente', name='vista_login_docente'),

	#urls menu administracion departamentos academicos
	url(r'^administration/deptos_academics/$', 'view_administration_deptos_academics', name='vista_administracion_deptos_academics'),	
	url(r'^administration/deptos_academics/add/$', 'view_depto_academic_add', name='vista_nuevo_depto_academic'),	
	url(r'^administration/deptos_academics/details/(?P<idda>\d+)/$', 'view_depto_academic_edit', name='vista_detalle_deptoacademic'),	
	url(r'^administration/deptos_academics/delete/(?P<id_>\d+)/$', 'view_delete_depto_academic', name='vista_borrar_deptoacademic'),	

	#urls menu administracion de carreras
	url(r'^administration/carreras/$', 'view_administration_carreras', name='vista_administracion_carreras'),	
	url(r'^administration/carreras/add/$', 'view_carrera_add', name='vista_nueva_carrera'),	
	url(r'^administration/carreras/details/(?P<id_>\d+)/$', 'view_carrera_edit', name='vista_detalle_carreras'),	
	url(r'^administration/carreras/delete/(?P<id_>\d+)/$', 'view_delete_carrera', name='vista_borrar_carrera'),

	#urls menu administracion de documentos
	url(r'^administration/document/$', 'view_administration_documentos', name='vista_administracion_documentos'),	
	url(r'^administration/document/add/$', 'view_documento_add', name='vista_nuevo_documento'),	
	url(r'^administration/document/details/(?P<id_>\d+)/$', 'view_documento_edit', name='vista_detalle_documentos'),	
	url(r'^administration/document/delete/(?P<id_>\d+)/$', 'view_delete_documento', name='vista_borrar_documentos'),

	#urls menu administracion de asignaturas
	url(r'^administration/asignatura/$', 'view_administration_asignaturas', name='vista_administracion_asignaturas'),	
	url(r'^administration/asignatura/add/$', 'view_asignatura_add', name='vista_nueva_asignatura'),	
	url(r'^administration/asignatura/details/(?P<id_>\d+)/$', 'view_asignatura_edit', name='vista_detalle_asignaturas'),	
	url(r'^administration/asignatura/delete/(?P<id_>\d+)/$', 'view_delete_asignatura', name='vista_borrar_asignaturas'),

	#urls menu administracion de persona docente
	url(r'^censo/docente/add/$', 'view_add_people_docente', name='vista_nuevo_docente'),
	url(r'^censo/personadocente/edit/$', 'view_persona_docente_edit', name='vista_persona_docente_detalle'),
	url(r'^censo/docente/edit/$', 'view_senso_docente_edit', name='vista_senso_docente_detalle'),

	#urls menu administracion de tipo de asignaturas
	url(r'^administration/tipo_asignatura/$', 'view_administration_type_subject', name='vista_administracion_tipo_asignaturas'),
	url(r'^administration/tipo_asignatura/add/$', 'view_type_subject_add', name='vista_nueva_tipo_asignatura'),	
	url(r'^administration/tipo_asignatura/details/(?P<idta>\d+)/$', 'view_type_subject_edit', name='vista_detalle_tipo_asignaturas'),
	url(r'^administration/tipo_asignatura/delete/(?P<idta>\d+)/$', 'view_type_subject_delete', name='vista_borrar_tipo_asignaturas'),


	#urls tipos de condiciones matricula
	url(r'^administration/tipo_condiciones_m/$', 'view_administration_enrollment_conditions', name='vista_administracion_tipo_cm'),
	url(r'^administration/tipo_condiciones_m/add/$', 'view__enrollment_conditions_add', name='vista_nuevo_tipo_cm'),	
	url(r'^administration/tipo_condiciones_m/details/(?P<idtcm>\d+)/$', 'view_enrollment_conditions_edit', name='vista_detalle_tipo_cm'),
	url(r'^administration/tipo_condiciones_m/delete/(?P<idtcm>\d+)/$', 'view_enrollment_conditions_delete', name='vista_borrar_tipo_cm'),

	#urls tipos de condiciones matricula
	url(r'^administration/secciones/$', 'view_administration_secciones', name='vista_administracion_secciones'),
	url(r'^administration/secciones/add/$', 'view__secciones_add', name='vista_nueva_seccion'),	
	url(r'^administration/secciones/details/(?P<idtcm>\d+)/$', 'view_secciones_edit', name='vista_detalle_secciones'),
	url(r'^administration/secciones/delete/(?P<idtcm>\d+)/$', 'view_secciones_delete', name='vista_borrar_secciones'),
	url(r'^administration/secciones/horario/(?P<idtcm>\d+)/$', 'view_secciones_horario', name='vista_secciones_horario'),

	#urls requisitos de las asignaturas
	url(r'^administration/requisitos/$', 'view_administration_requirements', name='vista_administracion_requisito'),
	url(r'^administration/requisitos/add/$', 'view_requirements_add', name='vista_nuevo_requisito'),
	url(r'^administration/requisitos/ajaxlab/$', 'view_requirements_ajax_uv', name='vista_requisitos_ajax_laboratorio'),
	url(r'^administration/requisitos/addsubjects/$', 'view_requirements_add_subjects', name='vista_nuevo_requisito_asignatura'),
	url(r'^administration/requisitos/ajaxsubjects/$', 'view_requirements_ajax_uv_subjects', name='vista_requisitos_ajax_asignatura'),
	url(r'^administration/requisitos/ajaxlist/$', 'view_requirements_ajax_list', name='vista_requisitos_ajax_listar'),
	url(r'^administration/requisitos/updateajax/$', 'view_requirements_ajax_update', name='vista_ajax_actualizar_requerimientos'),
	url(r'^administration/requisitos/delete/(?P<idtcm>\d+)/$', 'view_requirements_delete', name='vista_borrar_requisitos'),
	url(r'^administration/requisitos/edit/(?P<idtcm>\d+)/$', 'view_requirements_edit', name='vista_detalle_requisitos'),

	url(r'^administration/censo/$', 'view_administration_censo', name='vista_administracion_censo'),
	url(r'^administration/censo/avance$', 'view_avance_censo', name='vista_avance_censo'),
	url(r'^administration/censo/recuperar/clave$', 'view_recuperar_clave', name='vista_recuperar_clave'),

)
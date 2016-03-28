from django.conf.urls import patterns, url

urlpatterns = patterns('UNAG.apps.general.views',
	#urls menu administracion campus
	url(r'^administration/campus/$', 'view_administration_campus', name='vista_administracion_campus'),	
	url(r'^administration/campus/add/$', 'view_campus_add', name='vista_nuevo_campus'),
	url(r'^administration/campus/details/(?P<idcampus>\d+)/$', 'view_campus_edit', name='vista_detalle_campus'),
	url(r'^administration/campus/delete/(?P<idcampus>\d+)/$', 'view_delete_campus', name='vista_borrar_campus'),
	
	
	#urls menu de administracion de edificios
	url(r'^administration/buildings/$', 'view_administration_buildings', name='vista_administracion_edificios'),	
	url(r'^administration/buildings/add/$', 'view_buildings_add', name='vista_nuevo_edificio'),	
    url(r'^administration/buildings/details/(?P<idde>\d+)/$', 'view_buildings_edit', name='vista_detalle_edificios'),
    url(r'^administration/buildings/delete/(?P<idde>\d+)/$', 'view_delete_buildings', name='vista_borrar_edificios'),

    #urls menu de administracion de centros
	url(r'^administration/center/$', 'view_administration_centros', name='vista_administracion_centros'),	
	url(r'^administration/center/add/$', 'view_centro_add', name='vista_nuevo_centro'),	
    url(r'^administration/center/details/(?P<id_>\d+)/$', 'view_centro_edit', name='vista_detalle_centros'),
    url(r'^administration/center/delete/(?P<id_>\d+)/$', 'view_delete_centro', name='vista_borrar_centros'),

	#urls menu administracion de asociacionea academicas
	url(r'^administration/peasant_asociation/$', 'view_administration_peasant_asociation', name='vista_administracion_peasant_asociation'),		

	#urls menu administracion de centros regionales
	url(r'^administration/regional_centers/$', 'view_administration_regional_centers', name='vista_administracion_centros_regionales'),	
	
	#urls menu administracion de zonas
	url(r'^administration/zones/$', 'view_administration_zones', name='vista_administracion_zonas'),	
	
	#urls menu administracion de documentos
	url(r'^administration/documents/$', 'view_administration_documents', name='vista_administracion_documentos'),	
	
	#urls menu de administracion de jornada laboral
	url(r'^administration/workdays/$', 'view_administration_workdays', name='vista_administracion_jornadas_laborales'),	
	
	#urls menu de administracion de usuarios
	url(r'^administration/users/$', 'view_administration_users', name='vista_administracion_usuarios'),	
	
	#urls menu de administracion de estudiantes
	url(r'^administration/students/$', 'view_administration_students', name='vista_administracion_estudiantes'),	
	
	#urls menu de administracion de docentes
	url(r'^administration/profesor/$', 'view_administration_teachers', name='vista_administracion_profesores'),	
	
	#urls menu de administracion de edificios
	url(r'^administration/buildings/$', 'view_administration_buildings', name='vista_administracion_edificios'),	
	
	#urls menu de administracion de dormitorios
	url(r'^administration/bedroom/$', 'view_administration_bedroom', name='vista_administracion_dormitorios'),	
	url(r'^administration/bedroom/add/$', 'view_bedroom_add', name='vista_nuevo_dormitorio'),
	url(r'^administration/bedroom/details/(?P<iddo>\d+)/$', 'view_bedroom_edit', name='vista_detalle_dormitorio'),	
	url(r'^administration/bedroom/delete/(?P<iddo>\d+)/$', 'view_bedroom_delete', name='vista_borrar_dormitorio'),	
	url(r'^administration/bedroom/ajax/$', 'view_bedroom_ajax', name='vista_ajax_dormitorio'),	

	#urls menu administracion persona
	url(r'^administration/people/ajaxmuni/$', 'view_people_ajax_municipio', name='vista_persona_ajax_municipio'),

	#urls menu administracion personas recurso humano
	url(r'^administration/people/recursohumano/$', 'view_administration_recursohumano', name='vista_administracion_recursohumano'),
	url(r'^administration/people/add/recursohumano/normal$', 'view_add_recursohumano_normal', name='vista_nuevo_recursohumano_normal'),
	url(r'^administration/people/add/recursohumano/docente$', 'view_add_recursohumano_docente', name='vista_nuevo_recursohumano_docente'),
	url(r'^administration/people/recursohumano/recuperar$', 'view_recuperar_registro', name='vista_recuperar_registro'),

	#por Katherine
	url(r'^administration/ajax/ubicacion/$', 'ajax_ubicacion', name='ajax_ubicacion'),
	url(r'^periodo/registro/$', 'general_periodo_registro', name='general_periodo_registro'),
	url(r'^periodo/lista/$', 'general_periodo_lista', name='general_periodo_lista'),
	url(r'^administration/$', 'general_administration', name='general_administration'),
		
)


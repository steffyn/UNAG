from django.conf.urls import patterns, url

urlpatterns=patterns('UNAG.apps.home.views', 
		url(r'^$', 'view_login', name='vista_principal'),
		#url(r'^about/$', 'about_view', name='vista_about'),
		url(r'^accounts/login/$', 'view_login', name='vista_login'),
		url(r'^logout/$', 'view_logout', name='vista_logout'),
		url(r'^censo/$', 'view_home_senso', name='vista_inicio_senso'),
		url(r'^censo/logout/$', 'view_senso_logout', name='vista_senso_logout'),
		url(r'^main_first/$', 'view_main_first', name='vista_main_first'),
		url(r'^student/$', 'view_main_student', name='vista_main_student'),
		url(r'^profesor/$', 'view_main_teacher', name='vista_main_teacher'),
		url(r'^administration/$', 'view_main_administration', name='vista_main_administration'),
		url(r'^excel/$', 'view_excel', name='vista_excel'),
		url(r'^excel/docente$', 'view_excel_docente', name='vista_excel_docente'),
)
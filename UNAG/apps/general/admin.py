from django.contrib import admin
from models import *

class MyModelAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, ac_usuario_creador, request, **kwargs):
		if ac_usuario_creador.name == 'usuario_creador' or ac_usuario_creador.name == 'usuario_modificador':
			kwargs['initial'] = request.user.id
			return ac_usuario_creador.formfield(**kwargs)
		return super(MyModelAdmin, self).formfield_for_foreignkey(
			ac_usuario_creador, request, **kwargs
		)

class personaAdmin(admin.ModelAdmin):
	list_filter = ['tipo_persona']
	search_fields = ('identidad', 'nombres', 'apellidos')

	def formfield_for_foreignkey(self, ac_usuario_creador, request, **kwargs):
		if ac_usuario_creador.name == 'usuario_creador' or ac_usuario_creador.name == 'usuario_modificador':
			kwargs['initial'] = request.user.id
			return ac_usuario_creador.formfield(**kwargs)
		return super(personaAdmin, self).formfield_for_foreignkey(
			ac_usuario_creador, request, **kwargs
		)

admin.site.register(modalidades, MyModelAdmin)
admin.site.register(asoc_campesina, MyModelAdmin)
admin.site.register(zona, MyModelAdmin)
admin.site.register(tipo_administracion, MyModelAdmin)
admin.site.register(tipo_centro, MyModelAdmin)
admin.site.register(jornada, MyModelAdmin)
admin.site.register(estado_civil, MyModelAdmin)
admin.site.register(grupo_grado, MyModelAdmin)
admin.site.register(periodo, MyModelAdmin)
admin.site.register(periodo_clase, MyModelAdmin)
admin.site.register(persona, personaAdmin)
admin.site.register(tipo_beca, MyModelAdmin)
admin.site.register(tipo_edificios, MyModelAdmin)
admin.site.register(tipo_identificacion, MyModelAdmin)
admin.site.register(tipo_persona, MyModelAdmin)
admin.site.register(centro, MyModelAdmin)
admin.site.register(Titulos, MyModelAdmin)

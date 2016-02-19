from django.contrib import admin
from models import *

class alumnosAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, ac_usuario_creador, request, **kwargs):
		if ac_usuario_creador.name == 'usuario_creador' or ac_usuario_creador.name == 'usuario_modificador':
			kwargs['initial'] = request.user.id
			return ac_usuario_creador.formfield(**kwargs)
		return super(alumnosAdmin, self).formfield_for_foreignkey(
			ac_usuario_creador, request, **kwargs
		)
	list_display = ['persona', 'codigo_registro']
	search_fields = ('persona__identidad', 'persona__nombres', 'persona__apellidos', 'codigo_registro')

admin.site.register(Alumnos, alumnosAdmin)

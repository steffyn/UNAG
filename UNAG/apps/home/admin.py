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

class userAdmin(admin.ModelAdmin):
	list_display = ['username', 'codigo_registro', 'tipo_usuario']
	list_filter = ['tipo_usuario']
	search_fields = ('username',)

	def formfield_for_foreignkey(self, ac_usuario_creador, request, **kwargs):
		if ac_usuario_creador.name == 'usuario_creador' or ac_usuario_creador.name == 'usuario_modificador':
			kwargs['initial'] = request.user.id
			return ac_usuario_creador.formfield(**kwargs)
		return super(userAdmin, self).formfield_for_foreignkey(
			ac_usuario_creador, request, **kwargs
		)

admin.site.register(Rol, MyModelAdmin)
admin.site.register(TipoUsuario, MyModelAdmin)

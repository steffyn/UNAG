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

admin.site.register(Modalidades, MyModelAdmin)
admin.site.register(AsocCampesina, MyModelAdmin)
admin.site.register(Zona, MyModelAdmin)
admin.site.register(TipoAdministracion, MyModelAdmin)
admin.site.register(TipoCentro, MyModelAdmin)
admin.site.register(Jornada, MyModelAdmin)
admin.site.register(EstadoCivil, MyModelAdmin)
admin.site.register(GrupoGrado, MyModelAdmin)
admin.site.register(Periodo, MyModelAdmin)
admin.site.register(PeriodoClase, MyModelAdmin)
admin.site.register(Persona, personaAdmin)
admin.site.register(TipoBeca, MyModelAdmin)
admin.site.register(TipoEdificios, MyModelAdmin)
admin.site.register(TipoIdentificacion, MyModelAdmin)
admin.site.register(TipoPersona, MyModelAdmin)
admin.site.register(Centro, MyModelAdmin)
admin.site.register(Titulos, MyModelAdmin)

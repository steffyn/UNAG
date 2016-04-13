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

admin.site.register(JornadaLaboral, MyModelAdmin)
admin.site.register(TipoDocente, MyModelAdmin)
admin.site.register(Horario, MyModelAdmin)
admin.site.register(HorarioHora, MyModelAdmin)
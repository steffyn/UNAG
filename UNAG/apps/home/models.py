from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from datetime import datetime
# Create your models here.

class Rol(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='rol_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='rol_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		db_table='home_rol'
		permissions = (
			("can_view_menu", "Puede ver el menu de registro"),
			("can_view_home_censo", "Puede ver pantalla inicio censo"),
			("can_view_menu_registro", "Puede ver el menu de registro"),
			("can_recuperar_clave", "Puede recuperar clave de usuarios"),
			("can_view_avance_censo", "Puede ver el avance del censo"),
			("can_view_menu_censo", "Puede ver el menu del censo"),
		)

class TipoUsuario(models.Model):
	descripcion=models.CharField(max_length=512)
	usuario_creador=models.ForeignKey(User, related_name='tu_usuario_creador')
	fecha_creacion=models.DateField(auto_now_add=True)
	usuario_modificador=models.ForeignKey(User, related_name='tu_usuario_modificador')
	fecha_modificacion=models.DateField(auto_now=True)
	class Meta:
		db_table='home_tipo_usuario'

	def __unicode__(self):
		return self.descripcion

class User(User):
	
	user = models.OneToOneField(User)
	tipo_usuario = models.ForeignKey(TipoUsuario, null = True, blank = True,default = None)
	codigo_registro = models.CharField(max_length = 15, null = True, blank = True,default = None)
	telefono = models.CharField(max_length = 10, null = True, blank = True,default = None)
	direccion = models.CharField(max_length = 500, null = True, blank = True,default = None)
	class Meta:
		db_table='home_user'
	
	objects = UserManager()
	#user = models.ForeignKey(User, unique=True)

	# def __unicode__(self):
	#	return self.user.username


	def __unicode__(self):
		return self.user.username

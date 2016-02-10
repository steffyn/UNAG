from django.conf.urls import url
from UNAG.apps.descargas import views

urlpatterns = [
    url(r'^lista_centros/$', views.lista_centros, name='lista_centros'),
]
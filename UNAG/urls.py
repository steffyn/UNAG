from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UNAG.views.home', name='home'),
    # url(r'^UNAG/', include('UNAG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('UNAG.apps.home.urls')),
    url(r'^', include('UNAG.apps.alumnos.urls')),
    url(r'^', include('UNAG.apps.general.urls')),
    url(r'^', include('UNAG.apps.registro.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}) #permite el acceso a carpeta media
)

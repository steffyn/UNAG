import os
import sys

path='/var/www/UNAG'

if path not in sys.path:
 sys.path.append(path)

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SISCD.settings")
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
os.environ['DJANGO_SETTINGS_MODULE'] = 'UNAG.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

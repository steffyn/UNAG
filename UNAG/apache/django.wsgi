import os, sys
sys.path.append('/var/www/')
sys.path.append('/var/www/UNAG')

os.environ['DJANGO_SETTINGS_MODULE'] = 'UNAG.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
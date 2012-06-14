#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
# место, где лежит джанго
sys.path.append('/usr/lib/python2.7/dist-packages/django')
# место, где лежит проект
sys.path.append('/var/www/')
sys.stdout = sys.stderr
# файл конфигурации проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'cebuella.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

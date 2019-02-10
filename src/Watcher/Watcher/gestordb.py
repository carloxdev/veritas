# Python's Libraries
import os
import sys

# project_abspath = "C:\Users\Carlos\Proyectos\EstafetaConnect\src\GestorDB"
# project_abspath = os.path.abspath(os.path.join(os.getcwd(), 'CapaDatos'))
project_abspath = os.path.abspath(os.path.join(
    os.getcwd(), os.pardir, os.pardir, 'Exhibitor'))

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Exhibitor.settings")

# Django's Libraries
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Site's Models
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from configuration.models import Log
from newspaper.models import NewsItem


class ModeloNewsItem(object):

    @classmethod
    def add(self, _item):
        try:
            newsitem = NewsItem()
            newsitem.title = _item.get('title')
            newsitem.date = _item.get('date')
            newsitem.body = _item.get('body')
            newsitem.actors = _item.get('actors')
            newsitem.place = _item.get('place')
            newsitem.cover_img = _item.get('cover_img')
            newsitem.link = _item.get('link')
            newsitem.save()

            print("Dato guardado en BD")

        except Exception as e:
            print(str(e))

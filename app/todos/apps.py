from __future__ import unicode_literals

from django.apps import AppConfig


class TodosConfig(AppConfig):
    name = 'todos'
    verbose_name = 'TODOs sample application'

    default_auto_field = 'django.db.models.BigAutoField'

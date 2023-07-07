from django.apps import AppConfig


class KanbanBackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kanban_back'
    def ready(self):
        from .models import Tarefa, Coluna, Quadro
        from django.contrib import admin
        admin.site.register(Quadro)
        admin.site.register(Coluna)
        admin.site.register(Tarefa)

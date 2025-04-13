from django.apps import AppConfig


class AContactmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_contactme'

    def ready(self):
        from . import signals

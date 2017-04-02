from django.apps import AppConfig

class ArcaneConfig(AppConfig):
    name = 'Arcane'

    def ready(self):
        import arcane.signals

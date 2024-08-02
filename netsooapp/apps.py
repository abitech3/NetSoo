from django.apps import AppConfig


class NetsooappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "netsooapp"

    def ready(self):
        import netsooapp.signals
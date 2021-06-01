from django.apps import AppConfig


class PaperdetailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paperDetails'

    def ready(self):
        import paperDetails.signals
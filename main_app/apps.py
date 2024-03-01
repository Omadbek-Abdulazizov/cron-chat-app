from django.apps import AppConfig



class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

    def ready(self) -> None:
        from cron import updater
        updater.start()

    

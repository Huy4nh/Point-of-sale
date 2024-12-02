from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home'


class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import Home.signals
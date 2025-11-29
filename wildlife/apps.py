from django.apps import AppConfig


class WildlifeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wildlife"

def ready(self):
        from .models import create_sample_data
        create_sample_data()  # Call your function here
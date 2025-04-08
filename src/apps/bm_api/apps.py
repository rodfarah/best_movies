from django.apps import AppConfig


class BmApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "apps.bm_api"

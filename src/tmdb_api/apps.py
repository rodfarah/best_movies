from django.apps import AppConfig


class TmdbApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "tmdb_api"

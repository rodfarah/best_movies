from django.contrib import admin

from apps.bm_api.models import ActorOrActress, Director, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["full_name"]
    ordering = ["full_name"]


@admin.register(ActorOrActress)
class ActorOrActressAdmin(admin.ModelAdmin):
    list_display = ["full_name"]
    ordering = ["full_name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "director", "average_stars"]
    ordering = ["-average_stars"]

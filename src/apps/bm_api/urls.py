from django.urls import path

from . import views

app_name = "bm_api"

urlpatterns = [
    # List of all movie data objects available in DB
    path(
        "v1/movies/full-list/",
        views.MoviesListView.as_view(),
        name="complete_movies_list",
    )
]

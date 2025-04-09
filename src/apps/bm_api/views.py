from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import generics

from . import models, paginator, serializer


@extend_schema(
    summary="Movies List",
    description="Returns a paginated movies list with corresponding data",
    parameters=[
        OpenApiParameter(
            name="page", description="Page number", required=False, type=int
        ),
        OpenApiParameter(
            name="page_size",
            description="Items per page (max: 50)",
            required=False,
            type=int,
        ),
    ],
    responses={200: serializer.MovieDataSerializer(many=True)},
    examples=[
        OpenApiExample(
            name="movies_data_example",
            summary="Example movies data",
            description="A movie data record",
            value=[
                {
                    "title": "Movie title",
                    "director": "Director name",
                    "actors": ["Actor 1", "Actor 2"],
                    "average_stars": 4,
                },
                {
                    "title": "Movie title 2",
                    "director": "Director name 2",
                    "actors": ["Actor 3", "Actor 4"],
                    "average_stars": 5,
                },
            ],
            request_only=False,
            response_only=True,
            status_codes=["200"],
        )
    ],
)
class MoviesListView(generics.ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializer.MovieDataSerializer
    pagination_class = paginator.StandardPagination
    pagination_class = paginator.StandardPagination

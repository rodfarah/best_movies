from random import choice, choices

from faker import Faker

from .models import ActorOrActress, Director, Movie


class FakeCreator:
    def __init__(self):
        self.fake = Faker()

    def create_people_names(self, num_of_names) -> list[str]:
        return [self.fake.name() for _ in range(num_of_names)]

    def create_movie_titles(self, num_of_movies):
        return [self.fake.text(max_nb_chars=15) for _ in range(num_of_movies)]


class DatabaseCreator(FakeCreator):
    def create_database(
        self,
        num_of_movies: int,
        num_of_directors: int,
        num_of_actors: int,
        num_actors_per_movie: int,
    ) -> dict[str, str]:
        if (
            not (
                num_of_movies
                and num_of_directors
                and num_of_actors
                and num_actors_per_movie
            )
            > 0
        ):
            raise ValueError("All arguments must be 1 or higher")

        # generate fake data
        directors_name_list = self.create_people_names(num_of_directors)
        actor_or_actress_name_list = self.create_people_names(num_of_actors)
        movie_titles_list = self.create_movie_titles(num_of_movies)

        # Instantiate objects
        director_objects_list = [
            Director(full_name=name) for name in directors_name_list
        ]
        actor_or_actress_objects_list = [
            ActorOrActress(full_name=name) for name in actor_or_actress_name_list
        ]

        # bulk create directors and actors(or actresses)
        directors = Director.objects.bulk_create(director_objects_list)
        actors_or_actresses = ActorOrActress.objects.bulk_create(
            actor_or_actress_objects_list
        )

        # instantiate Movies
        for title in movie_titles_list:
            # generate random rating between 0 and 5
            stars = self.fake.random_int(min=1, max=5)
            movie = Movie.objects.create(
                title=title,
                director=choice(directors),
                average_stars=stars,
            )
            # add actors or actresses to the many-to-many relationship
            selected_actors = choices(actors_or_actresses, k=num_actors_per_movie)
            movie.actors.add(*selected_actors)
        return {
            "message": f"Database has been created successfully with {num_of_movies}"
            f" movies, {num_of_directors} directors and {num_of_actors} actors or "
            f"actresses. Each movie has {num_actors_per_movie} actors or actresses."
        }

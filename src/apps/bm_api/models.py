from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q


class Director(models.Model):
    full_name = models.CharField(max_length=120)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Director Name"
        verbose_name_plural = "Directors Names"


class ActorOrActress(models.Model):
    full_name = models.CharField(max_length=120)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Actor (Actress) Name"
        verbose_name_plural = "Actors (Actresses) Names"


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies",
        blank=False,
        null=True,
    )
    actors = models.ManyToManyField(
        ActorOrActress,
        related_name="movies",
        blank=False,
    )
    average_stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        # ensure max and min average rating values in db
        constraints = [
            CheckConstraint(
                check=Q(average_stars__gte=1) & Q(average_stars__lte=5),
                name="average_rating_between_1_and_5",
            )
        ]

from rest_framework import serializers

from . import models


class DirectorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ["full_name"]


class ActorOrActressDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActorOrActress
        fields = ["full_name"]


class MovieDataSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Movie
        fields = ["title", "director", "actors", "average_stars"]

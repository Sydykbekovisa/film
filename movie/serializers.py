from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Genre
from actor.serializers import ActorsSerializersList


class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    genre = GenreListSerializers(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'cover', 'release_data', 'genre']


class MovieDetailSerializers(serializers.ModelSerializer):
    genre = GenreListSerializers(many=True)
    actors = ActorsSerializersList(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieAddUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_rating(self, value):
        if value > 10 or value < 0:
            raise ValidationError('Рейтинг не может быть больше 10 и меньше 0')
        return value


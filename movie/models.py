from django.db import models

from actor.models import Actors


class Genre(models.Model):
    title = models.CharField(max_length=34, verbose_name='Наименование жанра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название фильма')
    director = models.CharField(max_length=50, verbose_name='Режиссер')
    description = models.TextField(verbose_name='Описание')
    release_data = models.DateField(verbose_name='Дата релиза')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг')
    duration = models.CharField(max_length=19, verbose_name='Длительность')
    cover = models.ImageField(upload_to='media/movie_art', verbose_name='Обложка')
    actors = models.ManyToManyField(Actors, verbose_name='Актеры')
    movie = models.FileField(upload_to='media/movie', null=True, blank=True, verbose_name='Фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

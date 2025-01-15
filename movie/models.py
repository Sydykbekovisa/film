from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    release_date = models.DateField(verbose_name='Дата релиза')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        help_text='Рейтинг должен быть от 1 до 10',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        null=True,
        blank=True
                                              )
    duration = models.CharField(max_length=19, verbose_name='Длительность фильма')
    cover = models.ImageField(upload_to='media/movie_art', verbose_name='Обложка')
    actors = models.ManyToManyField(Actors, verbose_name='Актеры')
    movie_file = models.FileField(upload_to='media/movie', null=True, blank=True, verbose_name='Фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

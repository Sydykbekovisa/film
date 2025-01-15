from django.db import models


class Actors(models.Model):
    name = models.CharField(max_length=34, verbose_name='Наименование актера')
    image = models.ImageField(upload_to='media/actors_art')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

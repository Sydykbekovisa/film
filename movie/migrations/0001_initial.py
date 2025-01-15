# Generated by Django 5.1.4 on 2025-01-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=34, verbose_name='Наименование жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Название фильма')),
                ('director', models.CharField(max_length=50, verbose_name='Режиссер')),
                ('description', models.TextField(verbose_name='Описание')),
                ('release_data', models.DateField(verbose_name='Дата релиза')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Рейтинг')),
                ('duration', models.CharField(max_length=19, verbose_name='Длительность')),
                ('cover', models.ImageField(upload_to='media/movie_art')),
                ('actors', models.ManyToManyField(to='actor.actors', verbose_name='Актеры')),
                ('genre', models.ManyToManyField(to='movie.genre', verbose_name='Жанр')),
            ],
        ),
    ]

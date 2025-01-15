# Generated by Django 5.1.4 on 2025-01-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie',
            new_name='movie_file',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='release_data',
            new_name='release_date',
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=19, verbose_name='Длительность фильма'),
        ),
    ]

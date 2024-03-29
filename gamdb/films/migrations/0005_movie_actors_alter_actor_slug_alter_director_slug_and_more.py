# Generated by Django 4.1.7 on 2023-06-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_actor_director_slug_movie_avg_rating_movie_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='films.actor'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='films.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(),
        ),
    ]

# Generated by Django 3.2.4 on 2021-11-27 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_jokes_joke_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokes',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jokes',
            name='joke_rating',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0002_album_artists"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album", name="releaseDate", field=models.DateField(),
        ),
    ]

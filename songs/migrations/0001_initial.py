# Generated by Django 4.1.2 on 2022-10-19 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("albums", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                ("image", models.ImageField(upload_to="images")),
                ("audio", models.FileField(upload_to="musics/")),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="albums.album"
                    ),
                ),
            ],
        ),
    ]

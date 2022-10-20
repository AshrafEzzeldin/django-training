# Generated by Django 4.1.2 on 2022-10-19 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("artists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
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
                ("creationDate", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(default="New Album", max_length=100)),
                ("releaseDate", models.DateTimeField()),
                ("cost", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "approved",
                    models.BooleanField(
                        default=False,
                        help_text="Approve the album if its name is not explicit",
                    ),
                ),
                (
                    "artists",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="artists.artist"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]

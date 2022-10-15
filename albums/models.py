from django.db import models

from artists.models import Artist


class Album(models.Model):
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="New Album")
    creationDate = models.DateTimeField(auto_now_add=True)
    releaseDate = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    approved = models.BooleanField(default=False,help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return "AlbumName is " + self.name

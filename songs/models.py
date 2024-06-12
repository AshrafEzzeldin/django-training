from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from albums.models import Album
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Song(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    audio = models.FileField(upload_to='music')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        if self.name == "":
            self.name = self.album.name


@receiver(post_delete, sender=Song)
def signal_function_name(sender, instance, using, **kwargs):
    try:
        print(len(Album.objects.filter(id=instance.album.id)[0].song_set.all()))
        if len(Album.objects.filter(id=instance.album.id)[0].song_set.all()) == 0:
            Album.objects.filter(id=instance.album.id).delete()
    except:
        pass

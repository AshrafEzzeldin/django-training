from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers

from users.models import User
from .models import Album
from .tasks import congrats


class AlbumSerializer(serializers.ModelSerializer):
    artists = serializers.ReadOnlyField(source="test")

    class Meta:
        model = Album
        fields = "__all__"


@receiver(post_save, sender=Album)
def send_congrats(sender, instance, created, **kwargs):
    congrats.delay(instance.name, instance.artists.stageName, User.objects.get(pk=instance.artists.owner_id).email)

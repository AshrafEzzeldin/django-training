from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    artists = serializers.ReadOnlyField(source="test")

    class Meta:
        model = Album
        fields = "__all__"

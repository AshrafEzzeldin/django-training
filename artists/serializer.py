from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="test")

    class Meta:
        model = Artist
        fields = '__all__'

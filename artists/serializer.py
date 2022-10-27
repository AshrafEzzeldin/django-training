from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='_is_my_find')

    def _is_my_find(self, obj):
        user_id = self.context.get("user_id")
        print(user_id)
        return user_id

    class Meta:
        model = Artist
        fields = '__all__'

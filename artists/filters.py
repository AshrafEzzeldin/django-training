from django_filters import rest_framework as filters

from albums.models import Album


class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'cost': ['gte', 'lte'],
            'name': ['icontains']
        }

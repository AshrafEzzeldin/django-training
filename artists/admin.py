from django.contrib import admin
from django.db.models import Count

from .models import Artist
from albums.models import Album


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    inlines = [
        AlbumInline,
    ]

    @staticmethod
    def approved_albums(obj):
        return Album.objects.filter(artists=obj, approved=True).count()

    list_display = ['stageName', 'approved_albums']


admin.site.register(Artist, ArtistAdmin)

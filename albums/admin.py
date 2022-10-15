from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creationDate',)


admin.site.register(Album, AlbumAdmin)

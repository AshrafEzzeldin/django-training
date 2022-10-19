from django.contrib import admin

from .forms import AtLeastOneRequiredInlineFormSet
from .models import Album
from songs.models import Song


class SongInline(admin.StackedInline):
    model = Song
    can_delete = False
    formset = AtLeastOneRequiredInlineFormSet
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        SongInline,
    ]

    readonly_fields = ('creationDate',)


admin.site.register(Album, AlbumAdmin)

from rest_framework import generics, status
from rest_framework.response import Response
from artists.filters import AlbumFilter
from artists.models import Artist
from artists.serializer import ArtistSerializer
from .permissions import Artist_perm
from .serializer import *


class AlbumView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [Artist_perm]

    queryset = Album.objects.filter(approved=True)
    serializer_class = AlbumSerializer

    filterset_class = AlbumFilter

    def get(self, request, *args, **kwargs):
        albums = self.list(self, request, *args, **kwargs)
        for idx, a in enumerate(albums.data['results']):
            albums.data['results'][idx]["artists"] = ArtistSerializer(
                Artist.objects.filter(album=list(a.items())[0][1]),
                many=True).data
        return Response(albums.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(artists=Artist.objects.filter(owner_id=self.request.user)[0])

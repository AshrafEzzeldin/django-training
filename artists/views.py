from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .serializer import *
from albums.serializer import *
from albums.models import *
from rest_framework import permissions


class ArtistView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        artists = self.list(self, request, *args, **kwargs)
        for idx, a in enumerate(artists.data['results']):
            artists.data['results'][idx]["albums"] = AlbumSerializer(
                Album.objects.filter(artists=list(a.items())[0][1]),
                many=True).data
        return Response(artists.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

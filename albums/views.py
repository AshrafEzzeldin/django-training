from rest_framework import permissions, generics
from .serializer import *


class AlbumView(generics.ListAPIView, generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

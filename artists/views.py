from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from albums.serializer import *

from .models import *
from albums.models import *


class ArtistView(APIView):

    def get(self, request):
        albs = Album.objects.select_related('artists')
        d = dict()
        for a in albs:
            d.setdefault(a.artists.id, []).append(AlbumSerializer(a).data)
        return Response(d, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

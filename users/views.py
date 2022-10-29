from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import status


class UserDetailsView(APIView):

    def get(self, request, id):
        try:
            serializer = UserSerializer(
                User.objects.filter(id=id)[0])
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        serializer = UserUpdateSerializer(data=request.data, instance=User.objects.get(pk=id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        serializer = UserUpdateSerializer(data=request.data, instance=User.objects.get(pk=id), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

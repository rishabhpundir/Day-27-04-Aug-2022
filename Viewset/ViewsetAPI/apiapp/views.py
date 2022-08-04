from .models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from apiapp.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        msg = 'User Data Added!'
        if serializer.is_valid():
            serializer.save()
            return Response(msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        msg = 'User Data Updated!'
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        msg = 'Partial User Data Updated!'
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        msg = 'User Data Deleted!'
        user.delete()
        return Response(msg)


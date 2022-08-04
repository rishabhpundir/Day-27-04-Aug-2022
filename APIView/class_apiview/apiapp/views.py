from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from apiapp.serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class UserAPI(APIView):
    def get(self, request, user_id=None, format=None):

        if user_id is not None:
                user = User.objects.get(pk=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data)

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        msg = 'User Data Added!'
        if serializer.is_valid():
            serializer.save()
            return Response(msg, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        msg = 'User Data Updated!'
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        msg = 'Partial User Data Updated!'
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors)

    def delete(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        msg = 'User Data Deleted!'
        user.delete()
        return Response(msg)





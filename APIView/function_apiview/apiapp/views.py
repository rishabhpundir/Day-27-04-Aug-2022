from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from apiapp.serializers import UserSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def user_info(request, user_id=None, format=None):

    if request.method == "GET":
        if user_id is not None:
                user = User.objects.get(pk=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data)

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        msg = 'User Data Added!'
        if serializer.is_valid():
            serializer.save()
            return Response(msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "PUT":
        user = User.objects.get(pk=user_id)
        msg = 'User Data Updated!'
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "PATCH":
        user = User.objects.get(pk=user_id)
        msg = 'Partial User Data Updated!'
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(msg)
        return Response(serializer.errors)


    elif request.method == "DELETE":
        user = User.objects.get(pk=user_id)
        msg = 'User Data Deleted!'
        user.delete()
        return Response(msg)





from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserModelViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [BasicAuthentication]   # setting added in settings.py file
    # permission_classes = [IsAuthenticated]

# class UserReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
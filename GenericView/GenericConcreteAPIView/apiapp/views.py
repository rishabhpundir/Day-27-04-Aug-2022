from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication

class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    






# ---------------------------------------------------------------------
# Separate API Views as indivitual classes
# ---------------------------------------------------------------------

# class UserList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserCreate(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRetrieve(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserUpdate(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDelete(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

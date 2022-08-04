from rest_framework.generics import GenericAPIView
from .models import User
from apiapp.serializers import UserSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.


# List and Create - 'pk' not required
class UserListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset= User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve, Update & Delete - 'pk' required
class UserRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset= User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

     








# class UserList(GenericAPIView, ListModelMixin):
#     queryset= User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class UserCreate(GenericAPIView, CreateModelMixin):
#     queryset= User.objects.all()
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UserRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset= User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class UserUpdate(GenericAPIView, UpdateModelMixin):
#     queryset= User.objects.all()
#     serializer_class = UserSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class UserDelete(GenericAPIView, DestroyModelMixin):
#     queryset= User.objects.all()
#     serializer_class = UserSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

     
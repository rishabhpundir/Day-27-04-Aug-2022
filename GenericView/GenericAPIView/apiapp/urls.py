from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('userapi', views.UserListCreate.as_view()),
    path('userapi/<pk>', views.UserRetrieveUpdateDelete.as_view()),

]

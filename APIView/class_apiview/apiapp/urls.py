from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('userapi', views.UserAPI.as_view()),
    path('userapi/<user_id>', views.UserAPI.as_view()),

]

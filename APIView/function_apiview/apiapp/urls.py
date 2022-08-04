from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('userapi', views.user_info),
    path('userapi/<user_id>', views.user_info),

]

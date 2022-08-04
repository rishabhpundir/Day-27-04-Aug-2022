from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# register viewset with router
router.register('userapi', views.UserModelViewset, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

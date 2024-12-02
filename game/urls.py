from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'steam-games', SteamGamesViewSet, basename='steamgames')

urlpatterns = [
    path('api/', include(router.urls)),
]
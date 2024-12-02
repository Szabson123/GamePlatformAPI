from rest_framework import serializers
from .models import UserGame, SteamGames

class UserGamesSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = ['id', 'user', 'name', 'appid', 'icon']
        

class SteamGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamGames
        fields = ['appid', 'name', 'uuid']
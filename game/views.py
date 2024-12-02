from django.shortcuts import render
import requests
from .serializers import SteamGamesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, status
import time
import orjson
from .models import SteamGames


def add_game_if_not_exists(appid, name):
    game = SteamGames.objects.filter(appid=appid).first()
    
    if not game:
        game = SteamGames(appid=appid, name=name)
        game.save() 
        print(f"Game {name} (appid: {appid}) added.")
    else:
        print(f"Game {name} (appid: {appid}) already exists.")
        
        
def update_steam_game_list():
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    
    data = orjson.loads(response.content)
    
    if "applist" in data and "apps" in data["applist"]:
        for game in data["applist"]["apps"]:
            appid = game["appid"]
            name = game["name"]
            
            # Dodajemy grę, jeśli nie istnieje
            add_game_if_not_exists(appid, name)
    
    
class SteamGamesViewSet(viewsets.ModelViewSet):
    queryset = SteamGames.objects.all()
    serializer_class = SteamGamesSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
        
    @action(detail=False, methods=['post'])
    def update_steam_games(self, request):
        update_steam_game_list()
        return Response({"message": "Steam game list updated successfully."}, status=status.HTTP_200_OK)
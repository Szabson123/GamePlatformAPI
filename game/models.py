from django.db import models
from user.models import CustomUser
import uuid

class UserGame(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    appid = models.IntegerField()
    icon = models.ImageField(blank=True, null=True)
    
    
class SteamGames(models.Model):
    appid = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=33)
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())
        super().save(*args, **kwargs)
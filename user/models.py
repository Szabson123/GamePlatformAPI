from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=15, blank=True, validators=[MinLengthValidator(5, message="Za krótkie")])
    identyficator = models.CharField(max_length=5, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return self.username
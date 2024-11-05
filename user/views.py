from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer
from .utils import generate_identyficator


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        
        user.identyficator = generate_identyficator()
        user.save()
        
        return user
    
from rest_framework import serializers
from .models import CustomUser
from drf_spectacular.utils import extend_schema_field


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nickname', 'password', 'identyficator']
        extra_kwargs = {'password': {'write_only': True}, 'identyficator': {'read_only': True},}
    
    def create(self, validated_data):
        user = CustomUser(
            username = validated_data['username'],
            email = validated_data['email'],
            nickname = validated_data['nickname'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
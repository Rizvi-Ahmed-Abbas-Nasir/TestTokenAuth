from lib2to3.pgen2 import token
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.get(user=user).key
        print(token)
        return user
  

        
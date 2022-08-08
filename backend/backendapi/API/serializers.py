
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from API.models import Lead
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.get(user=user).key
        print(token)
        return user

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"
  

        
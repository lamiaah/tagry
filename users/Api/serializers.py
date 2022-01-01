from django.db.models.fields import CharField
from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = '__all__'


    def create(self, validated_data):

        user = CustomUser(
            email = validated_data['email'],
            username = validated_data['username']
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()

        return user
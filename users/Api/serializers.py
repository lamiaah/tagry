from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(read_only = False)
    username = serializers.CharField(read_only = False)
    password = serializers.CharField(write_only = True)
    
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

   
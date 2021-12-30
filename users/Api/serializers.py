from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

    
  
class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','email', 'username', 'password']
    

    def save(self):
        account = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account
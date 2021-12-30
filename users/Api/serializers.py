from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

    
  
class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account
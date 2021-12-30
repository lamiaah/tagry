from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


  
#   class RegistrationSerializer(serializers.ModelSerializer):

#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def save(self):
#         account = CustomUser(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords do not match!'})

#         account.set_password(password)
#         account.save()
#         return account
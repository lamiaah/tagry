from django.db.models.fields import CharField
from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email')


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('pk', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def save(self, validated_data):
#         user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user


  
class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = [ 'id','email', 'username', 'password']
        read_only_fields = ('id',)
  

    def save(self):
        account = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account
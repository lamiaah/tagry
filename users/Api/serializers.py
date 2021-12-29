from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only = False)
    username = serializers.CharField(read_only = False)
    password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ['username' , 'email', 'password' ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
       return CustomUser.objects.create_user(**validated_data)





class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only = False)
    password = serializers.CharField(write_only = True)


    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    # email = serializers.EmailField(read_only = False)
    # username = serializers.CharField(read_only = False)
    # password = serializers.CharField(write_only = True)
    
    # class Meta:
    #     model = CustomUser
    #     fields = '__all__'


    # def create(self, validated_data):

    #     user = CustomUser(
    #         email = validated_data['email'],
    #         username = validated_data['username']
    #     )
    #     password = validated_data['password']
    #     user.set_password(password)
    #     user.save()

    #     return user

  
     
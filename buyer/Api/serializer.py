from rest_framework import serializers
from buyer.models import Buyer

from cities.models import Cities
from countries.models import Countries
from area.models import Area
from users.models import CustomUser


# class BuyerSerializer(serializers.ModelSerializer):

#     user_id = RegistrationSerializer(read_only=True)
#     name = serializers.CharField ()
#     about = serializers.CharField ()
#     image= serializers.ImageField ()
#     address = serializers.CharField()
#     city =  serializers.IntegerField()
#     country =  serializers.IntegerField()
#     area =  serializers.IntegerField()

#     class Meta:
#         model= Buyer
#         fields='__all__'


#     def create(self, validated_data):

     
#             user_id =validated_data.pop('user_id')
#             user_instance, created= CustomUser.objects.get(id=user_id)
#             byer = Buyer.objects.create(**validated_data, user_id=user_instance )
#             return byer






class BuyerSerializer(serializers.ModelSerializer):

    user_id = serializers.CharField()
    area = serializers.CharField()
    address = serializers.CharField()
    name = serializers.CharField ()
    about = serializers.CharField ()
    image= serializers.ImageField ()
    city =  serializers.IntegerField()
    country =  serializers.IntegerField()
  



    class Meta:
        model = Buyer
        fields = '__all__'



    def create(self, validated_data):

        buyer = Buyer(
            user_id = CustomUser.objects.get(pk = validated_data['user']),
            area = Area.objects.get(pk = validated_data['area']),
            address = validated_data['address'],
            name = validated_data['name'],
            about = validated_data['about'],
            image = validated_data['image'],
            city = Cities.objects.get(pk = validated_data['city']),
            country =Countries.objects.get(pk = validated_data['country']),
            

        )

        buyer.save()

        return buyer


    
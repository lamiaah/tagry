from rest_framework import serializers
from buyer.models import Buyer
from cities.models import Cities
from countries.models import Countries
from area.models import Area
from users.models import CustomUser


class BuyerSerializer(serializers.ModelSerializer):

    user_id = serializers.CharField()
    name = serializers.CharField ()
    about = serializers.CharField ()
    image= serializers.ImageField ()
    address = serializers.CharField()
    area = serializers.CharField()
    city =  serializers.IntegerField()
    country =  serializers.IntegerField()
  



    class Meta:
        model = Buyer
        fields = '__all__'



    def create(self, validated_data):

        buyer = Buyer(
            user_id = CustomUser.objects.get(pk = validated_data['user_id']),
            name = validated_data['name'],
            about = validated_data['about'],
            image = validated_data['image'],            
            address = validated_data['address'],
            area = Area.objects.get(pk = validated_data['area']),
            city = Cities.objects.get(pk = validated_data['city']),
            country =Countries.objects.get(pk = validated_data['country']),
        )

        buyer.save()

        return buyer


    
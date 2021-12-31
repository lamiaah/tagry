from rest_framework import serializers
from buyer.models import Buyer
from users.Api.serializers import RegistrationSerializer
from cities.models import Cities
from countries.models import Countries
from area.models import Area
from users.models import CustomUser


class BuyerSerializer(serializers.ModelSerializer):

    user_id = RegistrationSerializer(read_only=True)
    name = serializers.CharField ()
    about = serializers.CharField ()
    image= serializers.ImageField ()
    address = serializers.CharField()
    city =  serializers.IntegerField()
    country =  serializers.IntegerField()
    area =  serializers.IntegerField()

    class Meta:
        model= Buyer
        fields='__all__'


    def create(self, validate_data):

     
            user_id =validate_data.pop('user_id')
            user_instance= CustomUser.objects.get(id=user_id)
            byer = Buyer.objects.create(**validate_data, user_id=user_instance )
            return byer



    
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

        buyer = Buyer(
            
            name = validate_data['name'],
            about = validate_data['about'],
            address = validate_data['address'],
            city = Cities.objects.get(pk = validate_data['city']),
            country = Countries.objects.get(pk = validate_data['country']),
            area = Area.objects.get(pk = validate_data['area']),
            image = validate_data['image'],
        )

        buyer.save()

        return buyer
    def to_representation(self, instance):
        self.fields['user'] =  RegistrationSerializer(read_only=True)
        return super(BuyerSerializer, self).to_representation(instance)
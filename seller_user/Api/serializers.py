from rest_framework import serializers
from seller_user.models import Seller
from categories.models import Categories
from cities.models import Cities
from countries.models import Countries
from area.models import Area
from users.models import CustomUser

 

class SellerSerializer(serializers.ModelSerializer):
    user = serializers.CharField ()
    name = serializers.CharField ()
    about = serializers.CharField ()
    image= serializers.ImageField ()
    website = serializers.URLField()
    seller_address = serializers.CharField()
    category_id =  serializers.CharField ()
    city_name =  serializers.CharField ()
    country_name =  serializers.CharField ()
    area_name =  serializers.CharField ()
    

    class Meta:
        model= Seller
        fields='__all__'


    def create(self, validated_data):

        seller = Seller(
            user = CustomUser.objects.get(pk = validated_data['user']),
            name = validated_data['name'],
            website = validated_data['website'],
            about = validated_data['about'],
            seller_address = validated_data['seller_address'],
            city_name = Cities.objects.get(pk = validated_data['city_name']),
            country_name = Countries.objects.get(pk = validated_data['country_name']),
            area_name = Area.objects.get(pk = validated_data['area_name']),
            image = validated_data['image'],
            category_id = Categories.objects.get(pk= validated_data['category_id']),
        )

        seller.save()
        return seller
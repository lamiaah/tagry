from stores.models import SellerStores
from rest_framework import serializers
from seller_user.models import Seller
from cities.models import Cities
from countries.models import Countries
from area.models import Area


class SellerStoresSerializer(serializers.ModelSerializer):
  store_name =serializers.CharField(read_only=False)
  seller =  serializers.PrimaryKeyRelatedField(queryset = Seller.objects.all())
  store_address =serializers.CharField(read_only=False)
  store_city =  serializers.ReadOnlyField(source='store_city.city_name')
  store_country =  serializers.ReadOnlyField(source='store_country.country_name')
  store_area = serializers.ReadOnlyField(source='store_area.area_name')

  def create(self, validated_data):
    

    seller = SellerStores(
      seller_address = validated_data['seller_address'],
      store_city = Cities.objects.get(pk = validated_data['store_city']),
      store_country = Countries.objects.get(pk = validated_data['store_country']),
      store_area = Area.objects.get(pk = validated_data['store_area']),
    
    )

    seller.save()
    return seller

  class Meta:
    model = SellerStores
    fields = '__all__'
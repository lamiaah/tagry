from stores.models import SellerStores
from rest_framework import serializers
from products.models import Products
from users.models import CustomUser


class SellerStoresSerializer(serializers.ModelSerializer):
  seller =  serializers.ReadOnlyField(source='seller_id.id')
  store_address =serializers.CharField(read_only=False)
  store_city =  serializers.ReadOnlyField(source='store_city.city_name')
  store_country =  serializers.ReadOnlyField(source='store_country.country_name')
  store_area =  serializers.ReadOnlyField(source='store_area.area_name')


  def create(self, validate_data):
    return SellerStores.objects.create(**validate_data)  


    

  class Meta:
    model = SellerStores
    fields = '__all__'
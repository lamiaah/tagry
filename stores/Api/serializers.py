from stores.models import SellerStores
from rest_framework import serializers
from seller_user.models import Seller
from cities.models import Cities
from countries.models import Countries
from area.models import Area


class SellerStoresSerializer(serializers.ModelSerializer):

  seller =  serializers.PrimaryKeyRelatedField(queryset = Seller.objects.all())
  store_address =serializers.CharField(read_only=False)
  store_city =  serializers.PrimaryKeyRelatedField(queryset = Cities.objects.all())
  store_country =  serializers.PrimaryKeyRelatedField(queryset = Countries.objects.all())
  store_area =  serializers.PrimaryKeyRelatedField(queryset = Area.objects.all())


  def create(self, validate_data):
    return SellerStores.objects.create(**validate_data)  


    

  class Meta:
    model = SellerStores
    fields = '__all__'
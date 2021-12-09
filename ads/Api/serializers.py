from ads.models import Ads
from rest_framework import serializers
from products.models import Products
from users.models import CustomUser


class AdsSerializer(serializers.ModelSerializer):
  
  start_data =serializers.DateTimeField()
  end_data =serializers.DateTimeField()
  product = serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
  
  added_by = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
 


  def create(self, validate_data):
    return Ads.objects.create(**validate_data)  


    

  class Meta:
    model = Ads
    fields = '__all__'
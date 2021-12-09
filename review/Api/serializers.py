from review.models import Review
from rest_framework import serializers
from products.models import Products
from users.models import CustomUser


class ReviewSerializer(serializers.ModelSerializer):

  description = serializers.CharField(read_only =False)
  rate = serializers.IntegerField(read_only = False)
  products_id = serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
  user_id = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
  created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
  updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())


  def create(self, validate_data):
    return Review.objects.create(**validate_data)  


    

  class Meta:
    model = Review
    fields = ['description', 'created_user', 'updated_user' ,'rate','products_id','user_id']

  
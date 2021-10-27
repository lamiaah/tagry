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


  # def update(self, instance, validate_data):
  #   instance.description = validate_data.get('description', instance.description)
  #   instance.rate = validate_data.get('rate', instance.rate)
  #   instance.products_id = validate_data.get('products_id', instance.products_id)
  #   instance.user_id= validate_data.get('user_id', instance.user_id)
  #   instance.created_user = validate_data.get('created_user', instance.created_user)
  #   instance.updated_user = validate_data.get('updated_user', instance.updated_user )

    

  class Meta:
    model = Review
    fields = ['description', 'created_user', 'updated_user' ,'rate','products_id','user_id']

  
from productkeyword.models import Product_keyword
from rest_framework import serializers
from users.models import CustomUser 


class KeySerializer(serializers.Serializer):

  keyword_title = serializers.CharField(read_only =False)
  created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
  updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())

  def create(self, validate_data):
    return Product_keyword.objects.create(**validate_data)      


  class Meta:
    model = Product_keyword
    feilds = ['id','keyword_title','created_user','updated_user'] 
 
    
from rest_framework import serializers
from offers.models import Offers
from products.models import Products
from users.models import CustomUser

class offersSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    products_id = serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
    discount = serializers.FloatField(read_only=False)
    expired = serializers.BooleanField(read_only=False)
    start_at = serializers.DateField(read_only=False)
    end_at = serializers.DateField(read_only=False)
    created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    
    def create(self, validate_data):
        return Offers.objects.create(**validate_data)      


    class Meta:
        model=Offers
        fields=['id','products_id','discount','expired','start_at','end_at', 'created_user', 'updated_user']
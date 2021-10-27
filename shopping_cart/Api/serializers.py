from rest_framework import serializers
from shopping_cart.models import Shopping_cart, Shopping_cart_product
from users.models import CustomUser
from products.models import Products



class ShoppingProductSerializer(serializers.ModelSerializer):
    shopping_cart_product = serializers.PrimaryKeyRelatedField(queryset = Shopping_cart.objects.all())  
    product_id = serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
   
   
    class Meta:
        model = Shopping_cart_product
        fields = '__all__'
   
    def create(self, validated_data):
        product_shopping = Shopping_cart_product(
            shopping_cart_product = validated_data['shopping_cart_product'],
            product_id =  validated_data['product_id'],
        )
        product_shopping.save()
        return  product_shopping


class ShoppingCartSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    total_price = serializers.FloatField()
    created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
 
    class Meta:
        model = Shopping_cart
        fields = '__all__'

    def create(self, validated_data):
        shopping = Shopping_cart(
            user_id = validated_data['user_id'],
            total_price = validated_data['total_price'],
            created_user = validated_data['created_user'],
            updated_user = validated_data['updated_user'],
        )
        shopping.save()
        return  shopping   


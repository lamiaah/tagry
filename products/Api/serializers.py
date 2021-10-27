
from rest_framework import  serializers
from products.models import Products ,ProductImage
from seller_user.models import Seller
from categories.models import Categories
from users.models import CustomUser
from productkeyword.models import Product_keyword
from django.http.response import Http404

          
class ImageSerializers(serializers.ModelSerializer):
    product =  serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
    image = serializers.ImageField()

    class Meta:
            model = ProductImage
            fields = '__all__'


    def create(self,validated_data):
        product_image = ProductImage(
            image = validated_data['image'],
            product = validated_data['product']
        )
        product_image.save()
        return product_image

        
class ProductSerializer(serializers.ModelSerializer):
    seller_id =  serializers.PrimaryKeyRelatedField(queryset = Seller.objects.all())
    category_id = serializers.PrimaryKeyRelatedField(queryset = Categories.objects.all())
    product_title = serializers.CharField(read_only=False)
    product_description = serializers.CharField(read_only=False)
    product_price = serializers.FloatField(read_only=False)
    product_hight = serializers.IntegerField(read_only=False)
    product_width = serializers.IntegerField(read_only=False)
    product_weight = serializers.FloatField(read_only=False)
    created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    keyword_title = serializers.PrimaryKeyRelatedField(queryset = Product_keyword.objects.all())

    class Meta:
        model = Products
        fields = '__all__'

    def create(self,validated_data):
        product= Products(
            seller_id = validated_data['seller_id'],
            category_id = validated_data['category_id'],
            product_title= validated_data['product_title'],
            product_description = validated_data['product_description'],
            product_price= validated_data['product_price'],
            product_hight = validated_data['product_hight'],
            product_width = validated_data['product_width'],
            product_weight = validated_data['product_weight'],
            keyword_title = validated_data['keyword_title'],
            created_user = validated_data['created_user'],
            updated_user = validated_data['updated_user'],
        )
        product.save()
        return product
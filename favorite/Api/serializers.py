from rest_framework import serializers
from favorite.models import Favorite
from users.models import CustomUser
from products.models import Products

class FavoriteSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only =True)
    products_id =  serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
    users_id = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    

    def create(self, validate_data):
        return Favorite.objects.create(**validate_data)      

    class Meta:
        model =Favorite
        fields =['id','products_id','user_id']

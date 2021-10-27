from rest_framework import serializers
from recently_view.models import Recently_view
from products.models import Products
from users.models import CustomUser

class RecentlyViewSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    products_id = serializers.PrimaryKeyRelatedField(queryset = Products.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    view_at = serializers.DateField(read_only=False)

    def create(self, validate_data):
        return Recently_view.objects.create(**validate_data)      

        
    class Meta:
        model = Recently_view
        fields =['id','products_id','user_id','view_at']
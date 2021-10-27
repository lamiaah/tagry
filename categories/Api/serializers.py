
from rest_framework import serializers
from categories.models import Categories
from users.models import CustomUser

class CategorySerializer(serializers.ModelSerializer):
    
    category_title = serializers.CharField(read_only=False)
    category_image  = serializers.ImageField(read_only =False)
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    created_by = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    updated_by = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())


    def create(self, validate_data):
        return Categories.objects.create(**validate_data)      

    class Meta:
        model= Categories
        fields ='__all__'
        

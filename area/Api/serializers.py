from django.db import models
from rest_framework import serializers
from area.models import Area

class AreaSerializer(serializers.ModelSerializer):
    city_name =  serializers.ReadOnlyField(source='city_name.city_name')
    country_name =  serializers.ReadOnlyField(source='country_name.country_name')
    area_name = serializers.CharField(read_only=True)
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    # country_name = serializers.RelatedField(read_only = True)
    # city_name = serializers.RaletedField(read_only = True)
    
    
    class Meta:
        model= Area
        fields =['id','area_name','country_name','city_name']

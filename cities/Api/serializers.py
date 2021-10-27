from rest_framework import serializers
from cities.models import Cities

class CitiesSerailizer(serializers.ModleSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only =True)
    city_name = serializers.CharField(read_only =True)
    country_name = serializers.RelatedField(read_only = True)



    class Meta:
        model=Cities
        fields=['id','city_name','country_name']
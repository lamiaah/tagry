# from rest_framework import serializers
# from countries.models import Countries

# class CountriesSerailizer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField(read_only =True)
#     user_id = serializers.PrimaryKeyRelatedField(read_only = True)
#     code = serializers.CharField(read_only = True)
#     country_name = serializers.CharField (read_only =True)
#     country_lanuage_code = serializers.RelatedField(read_only =True)
#     phone_code = serializers.CharField(read_only = True)

#     def create(self, validate_data):
#        return Countries.objects.create(**validate_data)  
#     class Meta:
#         model=Countries
#         fields=['id','user_id','code','country_name','country_language_code','phone_code']
        
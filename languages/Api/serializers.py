from rest_framework import serializers
from languages.models import Languages


class LanguagesSerializer(serializers.ModelSerializer):
    
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    language_code = serializers.CharField(read_only = True)
    language_name = serializers.CharField(read_only = True)

    
    
    
    class Meta:
        model = Languages
        fields = ['id','language_code','language_name']
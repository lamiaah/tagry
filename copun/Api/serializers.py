from copun.models import Copun
from rest_framework import serializers
from products.models import Products
from users.models import CustomUser


class CopunSerializer(serializers.ModelSerializer):
  copun_text = serializers.CharField()
  copun_value =  serializers.IntegerField()
  copun_status = serializers.CharField()

  def create(self, validate_data):
    return Copun.objects.create(**validate_data)  

  class Meta:
    model = Copun
    fields = '__all__'
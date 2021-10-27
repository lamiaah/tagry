from rest_framework import serializers
from purchase.models import Purchase
from users.models import CustomUser
from shopping_cart.models import Shopping_cart, Shopping_cart_product
class PurchaseSerailizer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    shopping_cart_id = serializers.PrimaryKeyRelatedField(queryset = Shopping_cart.objects.all())
    Shopping_cart_product =serializers.PrimaryKeyRelatedField(queryset = Shopping_cart_product.objects.all())
    status = serializers.CharField(read_only=False)
    created_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    updated_user = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())

    def create(self, validate_data):
        purchase = Purchase (
            shopping_cart_id = validate_data['shopping_cart_id'],
            Shopping_cart_product =validate_data['Shopping_cart_product'],
            status = validate_data['status'],
            created_user = validate_data['created_user'],
            updated_user = validate_data['updated_user']
        )
        purchase.save()
        return purchase     

    class Meta:
        model=Purchase
        fields = '__all__'
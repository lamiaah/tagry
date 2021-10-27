
from django import forms
from seller_user.models import Seller


class SellerForm(forms.ModelForm):
    class Meta : 
        model = Seller
        fields = '__all__'

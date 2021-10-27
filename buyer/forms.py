from django import forms
from buyer.models import Buyer


class BuyerForm(forms.ModelForm):
    class Meta : 
        model = Buyer
        fields = '__all__'

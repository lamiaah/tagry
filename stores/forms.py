from django import forms
from django.forms.fields import DateField
from stores.models import SellerStores
from django.conf import settings


class StoresForm(forms.ModelForm):


    class Meta:
        model = SellerStores
        fields = ['store_name','store_address', 'store_country', 'store_city','store_area','is_archived']



class EditStoresForm(forms.ModelForm):

    class Meta:
        model = SellerStores
        fields = ['store_name', 'store_address','store_country', 'store_city','store_area','is_archived']
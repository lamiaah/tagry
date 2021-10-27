from django import forms
from cities.models import Cities


class CityForm(forms.ModelForm):
    class Meta : 
        model = Cities
        fields =["city_name","country_name"]
     
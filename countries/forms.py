from django import forms
from countries.models import  Countries


class CountryForm(forms.ModelForm):
    class Meta : 
        model = Countries
        fields =["user_id","code","country_name","country_language_code","phone_code"]
        
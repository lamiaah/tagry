from django import forms
from area.models import Area


class AreaForm(forms.ModelForm):
    class Meta : 
        model = Area
        fields =["area_name","country_name","city_name"
        ]
        
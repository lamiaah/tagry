from django import forms
from languages.models import Languages


class LanguagesForm(forms.ModelForm):
    class Meta : 
        model = Languages
        fields =["language_code","language_name"]
        
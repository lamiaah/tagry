from django import forms
from productkeyword.models import Product_keyword


class KeyForm(forms.ModelForm):
    class Meta : 
        model = Product_keyword
        fields =["keyword_title"
        ]
        
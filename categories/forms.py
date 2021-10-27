from django import forms
from categories.models import Categories


class CategoryForm(forms.ModelForm):
    class Meta : 
        model = Categories
        fields =["category_title","category_image"]
        
 
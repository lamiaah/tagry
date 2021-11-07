from django import forms
from categories.models import Categories ,SubCategory


class CategoryForm(forms.ModelForm):
    class Meta : 
        model = Categories
        fields =["category_title","category_image"]
        
 


class SubCategoryForm(forms.ModelForm):
    class Meta : 
        model = SubCategory
        fields =["category_id","sub_title","sub_image"]
        

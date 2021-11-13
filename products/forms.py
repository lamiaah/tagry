from django import forms
from products.models import ProductImage ,Products


class ProductForm(forms.ModelForm):
    class Meta : 
        model = Products
        fields = ["category_id","product_title","product_description","product_price","product_hight","product_width","product_weight","keyword_title"]
        
 


class ImageForm(forms.ModelForm):

 
    class Meta : 
        model = ProductImage
        fields =["images"]
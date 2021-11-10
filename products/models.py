from django.db import models
from categories.models import Categories
from seller_user.models import Seller
from users.models import CustomUser
from  productkeyword.models import Product_keyword
from django.urls import reverse


class Products(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.RESTRICT )
    category_id = models.ForeignKey(Categories, on_delete= models.RESTRICT, related_name='+')
    is_archived = models.BooleanField(null= False, blank= False, default= False)
    product_title = models.CharField(null= False,blank=False,default='',max_length=75)
    product_description = models.CharField(null= False,blank=False ,max_length=225)
    product_price = models.FloatField(null= False,blank= False,default=0.0)
    product_hight = models.IntegerField(null= False,blank= False ,default=0)
    product_width = models.IntegerField(null= False,blank= False,default=0)
    product_weight = models.FloatField(null= False,blank= False ,default=0.0)
    keyword_title = models.ForeignKey(Product_keyword, on_delete=models.RESTRICT,related_name='+')
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False,  auto_now=True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')

    


    def __str__(self):
        return str(self.product_title)

    def get_absolute_url(self):
        return reverse('product_details', kwargs={ "pk": self.pk })        

 
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_pic/')
    product = models.ForeignKey(Products,on_delete= models.RESTRICT ,related_name='+') 
  


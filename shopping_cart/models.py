from django.db import models
from products.models import Products
from users.models import CustomUser

class Shopping_cart(models.Model):

    id = models.AutoField(null=False,blank=False,primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete= models.RESTRICT ,related_name='+')
    total_price = models.FloatField(null=False,blank=False,default=0.0)
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False,  auto_now=True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
        return str (self.id)
    
class Shopping_cart_product(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    shopping_cart_product = models.ForeignKey( Shopping_cart, on_delete=models.RESTRICT , related_name= '+')
    product_id = models.ForeignKey(Products,on_delete=models.RESTRICT,related_name='+')
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
      return str (self.product_id)
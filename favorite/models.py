from django.db import models
from products.models import Products
from users.models import CustomUser


class Favorite(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    products_id = models.ForeignKey(Products,on_delete=models.RESTRICT)
    is_archived = models.BooleanField(null= False, blank= False, default= False)
    users_id = models.ForeignKey(CustomUser , on_delete= models.RESTRICT ,related_name='+')
    added_at = models.DateField(auto_now=True)
    
   
    def __str__(self):
        return str(self.products_id)
    
   


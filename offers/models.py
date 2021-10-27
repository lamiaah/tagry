from django.db import models
from products.models import Products
from users.models import CustomUser


class Offers(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    products_id = models.ForeignKey(Products,on_delete=models.RESTRICT,related_name='products_title')
    is_archived = models.BooleanField(null= False, blank= False, default= False)
    discount = models.FloatField(null=False,blank=False,default=0.0)
    expired = models.BooleanField(null=True,blank=False ,default=False)
    numof_redem = models.IntegerField(null=False,blank=False,default=0)
    created_at = models.DateField(null= False, blank= False, auto_now=True)
    updated_at = models.DateField( null=False,blank=False , auto_now=True)
    start_at = models.DateField(null= True, blank= True)
    end_at = models.DateField(null= True, blank= True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')

    link = models.URLField()


    def __str__(self):
        return  str(self.products_id)
  


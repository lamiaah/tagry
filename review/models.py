from django.db import models
from products.models import Products
from users.models import CustomUser

class Review(models.Model):
    id  = models.AutoField(null=False,blank=False,primary_key=True)
    products_id = models.ForeignKey(Products,on_delete=models.RESTRICT)
    user_id = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+') 
    description  = models.CharField(null= False,blank=False ,max_length=225)
    rate  = models.IntegerField(null= False,blank= False,default=0)
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False , auto_now=True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
        return str('Products: {}'.format(self.products_id))
    

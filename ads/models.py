from django.db import models
from products.models import Products
from users.models import CustomUser



class Ads(models.Model):

    id =  models.AutoField(null=False,blank=False,primary_key=True)
    product = models.ForeignKey(Products, on_delete= models.RESTRICT)
    start_date = models.DateField(null= False, blank= False)
    end_date = models.DateField(null= False, blank= False)
    added_by = models.ForeignKey(CustomUser, on_delete= models.RESTRICT)
    is_archived = models.BooleanField(null= False, blank= False, default= False)



    def __str__(self):
        return str(self.product)
from django.db import models
from products.models import Products
from users.models import CustomUser

class Recently_view(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    products_id = models.ForeignKey(Products,on_delete=models.RESTRICT)
    user_id = models.ForeignKey(CustomUser,on_delete=models.RESTRICT)
    view_at = models.DateField(null= False, blank= False, auto_now=True)


    def __str__(self):
       return str('products:{}'.format(self.products_id))



   

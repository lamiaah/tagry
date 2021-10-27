from django.db import models
from users.models import CustomUser
from products.models import Products


class Popular(models.Model):
    id = models.AutoField(null=False, blank= False ,primary_key= True)
    product_id = models.ForeignKey( Products,on_delete= models.RESTRICT, related_name='+')
    created_date = models.DateField(null= False, blank= False, auto_now= True)
    updated_date = models.DateField(null= False, blank= False, auto_now= True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')


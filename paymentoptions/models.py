from django.db import models
from users.models import CustomUser


class PaymentOption(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    option_name = models.CharField(null= False, blank= False, default= '', max_length= 35, unique= True)
    created_date = models.DateField(null= False, blank= False, auto_now= True)
    updated_date = models.DateField(null= False, blank= False, auto_now= True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.option_name)
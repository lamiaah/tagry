from django.db import models
from users.models import CustomUser


class PaymentCurrency(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    currency_name = models.CharField(null= False, blank= False, default= '', max_length= 35, unique= True)
    currency_code = models.CharField(null= False, blank= False, default= '', max_length= 15, unique= True)
    created_date = models.DateField(null= False, blank= False, auto_now= True)
    updated_date = models.DateField(null= False, blank= False, auto_now= True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.currency_name + self.currency_code)
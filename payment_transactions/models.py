from django.db import models
from shopping_cart.models import Shopping_cart
from users.models import CustomUser
from paymentoptions.models import PaymentOption
from paymentcurrency.models import PaymentCurrency

class Payment(models.Model):
    id  = models.AutoField(null=False,blank=False,primary_key=True)
    shoppingcart_id = models.ForeignKey(Shopping_cart, on_delete=models.RESTRICT)
    is_archived = models.BooleanField(null= False, blank= False, default= False)
    transactions_data = models.DateTimeField(null= False, blank= False, auto_now=True)
    amount = models.IntegerField(null= False,blank= False ,default=0)
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False , auto_now=True)
    payment_options = models.ForeignKey(PaymentOption, on_delete= models.RESTRICT, related_name= '+')
    currency = models.ForeignKey(PaymentCurrency, on_delete= models.RESTRICT, related_name= '+')
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')


    def __str__(self):
        return str('shopping_cart:{}'.format(self.shoppingcart_id))




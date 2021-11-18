from django.db import models
from copun.models import Copun
from shopping_cart.models import Shopping_cart
from users.models import CustomUser


class Orders(models.Model):

    order_status_options = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
        ('delivering', 'delivering'),
        ('delivered', 'delivered'),
    )

    order_payment_options = (
        ('cach', 'cach'),
        ('visa', 'visa'),
    )

    id =  models.AutoField(null=False,blank=False,primary_key=True)
    order_status = models.CharField(null= False, blank= False, default= order_status_options[0], choices= order_status_options, max_length= 25)
    order_payment_option = models.CharField(null= False, blank= False, default= order_payment_options[0], choices= order_payment_options, max_length= 15)
    user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT)
    cart = models.ForeignKey(Shopping_cart, on_delete= models.RESTRICT)
    order_amount = models.FloatField(null= False, blank= False, default= 0.0)
    order_copun = models.ForeignKey(Copun, on_delete= models.RESTRICT, null= True)
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
        return str(f'User: {self.user}, Cart: {self.cart}')
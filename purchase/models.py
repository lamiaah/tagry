from shopping_cart.Api.views import shoppingcart_product
from django.db import models
from shopping_cart.models import Shopping_cart ,Shopping_cart_product
from users.models import CustomUser



class Purchase(models.Model):

    status_option = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('canceled', 'canceled')
    )

    id = models.AutoField(null=False,blank=False,primary_key=True)
 #   shopping_cart_id = models.ForeignKey(Shopping_cart, on_delete=models.RESTRICT)
#    shopping_cart_product = models.ForeignKey(Shopping_cart_product,on_delete= models.RESTRICT ,related_name='+')
    status = models.CharField(null= False, blank= False,default='',max_length=50, choices=status_option)
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False ,  auto_now=True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name='+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name='+')
    is_archived = models.BooleanField(null= False, blank= False, default= False)

   
   
   # def __str__(self):
  #      return str('shopping_cart:{}'.format(self.shopping_cart_id))



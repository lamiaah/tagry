from django.db import models
from area.models import Area
from cities.models import Cities
from seller_user.models import Seller
from countries.models import Countries


class SellerStores(models.Model):

    id =  models.AutoField(null=False,blank=False,primary_key=True)
    seller = models.ForeignKey(Seller, on_delete= models.RESTRICT)
    store_name = models.CharField(null= False, blank= False, default= '', max_length= 75)
    store_country = models.ForeignKey(Countries, on_delete= models.RESTRICT)
    store_city = models.ForeignKey(Cities, on_delete= models.RESTRICT)
    store_area = models.ForeignKey(Area, on_delete= models.RESTRICT)
    store_address = models.CharField(null= False, blank= False, default= '', max_length= 225)
    is_archived = models.BooleanField(null= False, blank= False, default= False)



    def __str__(self) -> str:
        return str(self.store_name)
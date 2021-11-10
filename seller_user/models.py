from django.db import models
from cities.models import Cities
from countries.models import Countries
from area.models import Area
from categories.models import Categories
from users.models import CustomUser
from django.urls import reverse

class Seller(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    name = models.CharField(null= False,blank=False,default='',max_length=75)
    about = models.CharField(null= False,blank=False ,max_length=225)
    image = models.ImageField(upload_to='seller_pic/')
    website = models.URLField(null= False, blank= False, default= '')
    seller_address = models.CharField(null= False, blank= False, default= '', max_length= 125)
    city_name = models.ForeignKey( Cities , on_delete= models.RESTRICT, related_name='+')
    country_name = models.ForeignKey(Countries,on_delete= models.RESTRICT, related_name='+')
    area_name = models.ForeignKey(Area, on_delete= models.RESTRICT, related_name='+')
    category_id = models.ForeignKey(Categories, on_delete=models.RESTRICT, related_name='+')
    is_archive = models.BooleanField(null=False,blank= False, default= False)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('seller_user:seller_detail', kwargs={ "pk": self.pk })   
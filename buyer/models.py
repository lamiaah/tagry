from django.db import models
from cities.models import Cities
from countries.models import Countries
from area.models import Area
from users.models import CustomUser

class Buyer(models.Model):
    id = models.AutoField(null=False,blank=False,primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete= models.RESTRICT, related_name='+')
    name = models.CharField(null= False,blank=False,default='',max_length=75)
    about = models.CharField(null= False,blank=False ,max_length=225)
    image = models.ImageField(upload_to='buyer_pic/')
    address = models.CharField(null= False, blank= False, default= '', max_length= 125)
    city = models.ForeignKey( Cities , on_delete= models.RESTRICT, related_name='+')
    country = models.ForeignKey(Countries,on_delete= models.RESTRICT, related_name='+')
    area = models.ForeignKey(Area, on_delete= models.RESTRICT, related_name='+')
    is_archive = models.BooleanField(null=False,blank= False, default= False)


    def __str__(self):
        return str(self.name)
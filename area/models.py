from django.db import models
from users.models import CustomUser
from countries.models import Countries
from cities.models import Cities


class Area(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    area_name = models.CharField(null= False, blank= False, default= '', max_length= 75, unique= True)
    country_name = models.ForeignKey(Countries, on_delete= models.RESTRICT, related_name= '+')
    city_name = models.ForeignKey(Cities, on_delete= models.RESTRICT, related_name= '+')
    area_created_date = models.DateField(null= False, blank= False, auto_now= True)
    area_updated_date = models.DateField(null= False, blank= False, auto_now= True)
    area_created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    area_updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.area_name )
    
        
   

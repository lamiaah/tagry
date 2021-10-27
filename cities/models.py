from users.models import CustomUser
from countries.models import Countries
from django.db import models




class Cities(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    city_name = models.CharField(null= False, blank= False, default= '', max_length= 75, unique= True)
    country_name = models.ForeignKey(Countries, on_delete= models.RESTRICT, related_name= '+')
    city_created_date = models.DateField(null= False, blank= False, auto_now= True)
    city_updated_date = models.DateField(null= False, blank= False, auto_now= True)
    city_created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    city_updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.city_name )
    
        
   

    
   

    
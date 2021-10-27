from users.models import CustomUser
from django.db import models
from languages.models import Languages
from users.models import CustomUser



class Countries(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    user_id = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    code = models.CharField(null= False, blank= False, default= '', max_length= 5, unique= True)
    country_name = models.CharField(null= False, blank= False, default= '', max_length= 75, unique= True)
    country_language_code = models.ForeignKey(Languages, on_delete= models.RESTRICT, related_name= '+')
    phone_code = models.CharField(null= False, blank= False, default= '', max_length= 25)
    country_created_date = models.DateField(null= False, blank= False, auto_now= True)
    country_updated_date = models.DateField(null= False, blank= False, auto_now= True)
    country_created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    country_updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.country_name)
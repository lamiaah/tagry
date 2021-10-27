from users.models import CustomUser
from django.db import models



class Languages(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    language_code = models.CharField(null= False, blank= False, default= '', max_length= 10, unique= True)
    language_name = models.CharField(null= False, blank= False, default= '', max_length= 50, unique= True)
    created_date = models.DateField(null= False, blank= False, auto_now= True)
    updated_date = models.DateField(null= False, blank= False, auto_now= True)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    updated_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')



    def __str__(self):
        return str(self.language_name)
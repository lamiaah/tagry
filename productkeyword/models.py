from django.db import models
from users.models import CustomUser

class Product_keyword(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    keyword_title = models.CharField(null= False, blank= False, max_length= 25, default= '')
    created_date = models.DateField(null=False, blank=False, auto_now=True)
    updated_date = models.DateField(null=False, blank=False, auto_now=True)
    created_user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='+')
    updated_user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='+')



    def __str__(self):
        return str(self.keyword_title)
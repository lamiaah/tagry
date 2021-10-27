from django.db import models
from users.models import CustomUser


class Noti(models.Model):

    id = models.AutoField(null=False,blank=False,primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='+')
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    send_at = models.DateTimeField( null=False,blank=False ,auto_now=True)
    image = models.ImageField(upload_to='noti_pic/')
    title = models.CharField(null=False,blank=False,default='',unique=True,max_length=50)
    description = models.CharField(null=False,blank=False,max_length=200)
    readed = models.BooleanField(null=False,blank=False,default=False)
    created_user = models.ForeignKey(CustomUser, on_delete= models.RESTRICT, related_name= '+')
    


    def __str__(self):
         return str(self.title)
    


from django.db import models



class Copun(models.Model):

    copun_status_options = (
        ('active', 'active'),
        ('deactive', 'deactive')
    )

    id =  models.AutoField(null=False,blank=False,primary_key=True)
    copun_text = models.CharField(null= False, blank= False, default= '', max_length= 75)
    copun_value = models.IntegerField(null= False, blank= False, default= 0)
    copun_status = models.CharField(null= False, blank= False, default= copun_status_options[0], choices= copun_status_options, max_length= 25)


    def __str__(self):
        return str(self.copun_text)
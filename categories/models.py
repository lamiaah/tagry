from django.db import models
from users.models import CustomUser
from django.urls import reverse


class Categories(models.Model):
    id  = models.AutoField(null=False,blank=False,primary_key=True)
    category_title = models.CharField(null= False,blank=False,default='',max_length=75, unique= True)
    category_image = models.ImageField(upload_to='category_pic/') 
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False,  auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT ,related_name='+',default='')
    updated_by = models.ForeignKey(CustomUser ,on_delete= models.RESTRICT ,related_name='+', default= '')
    is_archive = models.BooleanField(null= False ,blank= False ,default= False)

    def __str__(self):
        return str(self.category_title)
    
    def get_absolute_url(self):
        return reverse('cate_detail', kwargs={"id": self.pk})
    

class SubCategory(models.Model):
    id = models.AutoField(null=False ,blank= False,primary_key= True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_title = models.CharField(null= False,blank=False,default='',max_length=75, unique= True)
    is_archive = models.BooleanField(null= False ,blank= False ,default= False)
    sub_image = models.ImageField(upload_to='subcate_pic/') 
    created_at = models.DateTimeField(null= False, blank= False, auto_now=True)
    updated_at = models.DateTimeField( null=False,blank=False,  auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT ,related_name='+',default='')
    updated_by = models.ForeignKey(CustomUser ,on_delete= models.RESTRICT ,related_name='+', default= '')

    def __str__(self):
        return str(self.sub_title)

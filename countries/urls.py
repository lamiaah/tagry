from django.urls import path ,include
from .import views 


urlpatterns = [
    path('',views.area_list ,name= 'country'),
    path('add/',views.post , name= 'add_country')
    
]
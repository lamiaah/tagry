from django.urls import path ,include
from .import views 


urlpatterns = [
    path('',views.area_list ,name= 'key'),
    path('add/',views.post , name= 'add_key')
    
]
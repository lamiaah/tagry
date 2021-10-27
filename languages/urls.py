from django.urls import path ,include
from .import views 


urlpatterns = [
    path('',views.lan_list ,name= 'languages'),
    path('add/',views.post , name= 'add_languages')
    
]
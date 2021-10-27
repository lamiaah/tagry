from django.urls import path ,include
from .import views 


urlpatterns = [
    path('',views.city_list ,name= 'city'),
    path('add/',views.post , name= 'add_city')
]
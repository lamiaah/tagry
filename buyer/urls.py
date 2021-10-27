from django.urls import path
from . import views 

urlpatterns = [
    path('', views.buyer ,name='buyer_list'),
    path('<int:pk>/buyer', views.buyer_details, name= 'buyer_detail'),
    path('add_buyer/',views.post ,name= 'add_buyer'),
    path('<int:pk>/delete',views.delete ,name= 'delete_buyer'),
    ]

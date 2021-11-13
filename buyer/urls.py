from django.urls import path
from . import views 

urlpatterns = [
    path('', views.buyer ,name='buyer_list'),
    path('<int:pk>/buyer', views.buyer_details, name= 'buyer_detail'),
    path('add_buyer/<int:pk>',views.post ,name= 'add_buyer'),
    path('<int:pk>/delete',views.delete ,name= 'delete_buyer'),
    path('edit_buyer/<int:pk>/',views.edit,name='edit_buyer'),
    path('register_buyer/',views.buyer_regieter ,name= 'buyer_seller'),
    ]

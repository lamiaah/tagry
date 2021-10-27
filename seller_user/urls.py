from django.urls import path
from . import views 
app_name = 'seller_user'
urlpatterns = [
    path('', views.seller ,name='seller_list'),
    path('<int:pk>/seller', views.seller_details, name= 'seller_detail'),
    path('add_seller/',views.post ,name= 'add_seller'),
    path('<int:pk>/delete',views.delete ,name= 'delete'),
    ]

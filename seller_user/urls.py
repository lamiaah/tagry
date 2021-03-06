from django.urls import path
from . import views 
app_name = 'seller_user'
urlpatterns = [
    path('', views.seller ,name='seller_list'),
    path('<int:pk>/seller', views.seller_details, name= 'seller_detail'),
    path('register_seller/',views.seller_regieter ,name= 'register_seller'),
    path('add_seller/<int:pk>',views.post ,name= 'add_seller'),
    path('<int:pk>/delete',views.delete ,name= 'delete'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('search/',views.search,name='search'),
    ]

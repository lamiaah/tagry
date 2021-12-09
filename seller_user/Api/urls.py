from django.urls import path
from seller_user.Api.views import Get_Product, Get_Seller, RegisterSeller


urlpatterns = [
    path('register', RegisterSeller.as_view()),
    path('get_product/<int:seller_id>', Get_Product.as_view()),
    path('get_seller', Get_Seller.as_view()),
]

# from  django.urls import path
# from seller_user.Api.views import SellerApiList ,AddInfo ,UpdateInfo

# urlpatterns = [
#     path ('seller/',SellerApiList.as_view()),
#     path ('add/', AddInfo.as_view()),
#     path ('put/<int:id>/', UpdateInfo.as_view()),
# ]

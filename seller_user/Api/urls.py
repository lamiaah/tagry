from django.urls import path
from seller_user.Api.views import Get_Product, Get_Seller ,LoginSeller ,RegisterSeller ,GetSellerData


urlpatterns = [

    path('get_product/<int:seller_id>', Get_Product.as_view()),
    path('get_seller', Get_Seller.as_view()),
    path('info_seller/<int:user_id>',   GetSellerData.as_view()),
    path('register_seller/',RegisterSeller.as_view()),
    path('login_seller/',LoginSeller.as_view()),
]

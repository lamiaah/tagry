from django.urls import path
from buyer.Api.views import  BuyerInfo,RegisterBuyer,BuyerLogin


urlpatterns = [
    path('info/<int:user_id>',  BuyerInfo.as_view()),
    path('register_buyer/',RegisterBuyer.as_view()),
    path('login_buyer/',BuyerLogin.as_view()),
    
]

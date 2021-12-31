from django.urls import path
from buyer.Api.views import  BuyerLogin


urlpatterns = [
    path('info/',  BuyerLogin.as_view()),
    
]

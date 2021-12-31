from django.urls import path
from buyer.Api.views import  BuyerInfo


urlpatterns = [
    path('info/',  BuyerInfo.as_view()),
    
]

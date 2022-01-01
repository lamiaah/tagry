from django.urls import path
from buyer.Api.views import   RegisterBuyer ,LoginBuyer , GetBuyerData


urlpatterns = [
    path('info_buyer/<int:user_id>',   GetBuyerData.as_view()),
    path('register_buyer/',RegisterBuyer.as_view()),
    path('login_buyer/',LoginBuyer.as_view()),
    
]

from django.urls import path
from buyer.Api.views import BuyerInfo


urlpatterns = [
    path('info/<int:user_id>', BuyerInfo.as_view()),
    
]

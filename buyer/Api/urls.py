from django.urls import path
from buyer.Api.views import BuyerInfo


urlpatterns = [
    path('info/<int:id>', BuyerInfo.as_view()),
    
]

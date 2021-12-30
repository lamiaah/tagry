from django.urls import path
from buyer.Api.views import BuyerInfo


urlpatterns = [
    path('register/', BuyerInfo.as_view())
]

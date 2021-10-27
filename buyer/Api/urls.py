from django.urls import path
from buyer.Api.views import RegisterBuyer


urlpatterns = [
    path('register/', RegisterBuyer.as_view())
]

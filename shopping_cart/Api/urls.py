from django.urls import path
from shopping_cart.Api.views import ShoppingApi, AddShopping ,ShoppingPut

urlpatterns = [
    path('shopping/<int:user_id>/',ShoppingApi.as_view()),
    path('add/', AddShopping.as_view()),
    path('put/<int:id>/', ShoppingPut.as_view()),
    
]

from  django.urls import path
from purchase.Api.views import PurchaseApi ,AddPurchase ,DeleteProduct

urlpatterns = [
    path ('purchase/<int:shopping_cart>/',PurchaseApi.as_view()),
    path ('add/',AddPurchase.as_view()),
    path ('delete/<int:id>/',DeleteProduct.as_view()),
]
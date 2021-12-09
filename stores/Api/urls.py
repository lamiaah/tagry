
from django.urls import path
from stores.Api.views import SellerStoresList,SellerStoresAdd,PutSellerStores

urlpatterns = [
    path('all_stores/', SellerStoresList.as_view()),
    path('add/',SellerStoresAdd.as_view()),
    path('put/<int:id>/',PutSellerStores.as_view()),
    path('delete/<int:id>/',PutSellerStores.as_view()),
]
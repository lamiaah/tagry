from  django.urls import path
from products.Api.views import ProductApiList ,SearchApiCategory,SearchApiProduct , AddProduct ,PutProduct

urlpatterns = [
    path ('all/',ProductApiList.as_view()),
    path ('search/<int:category_id>/',SearchApiCategory.as_view()),
    path ('searchtitle/<str:product_title>/',SearchApiProduct.as_view()),
    path ('add/', AddProduct.as_view()),
    path ('put/<int:id>/', PutProduct.as_view()),
    path ('delete/<int:id>/', PutProduct.as_view()),
]
from django.urls import path
from . import views


urlpatterns = [
    path('allproduct/', views.get_products,name='all_product'),
    path('<int:category_id>/', views.get_bycategory),
    path('<str:product_title>/', views.get_byproduct),

]
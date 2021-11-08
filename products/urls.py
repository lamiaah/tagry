from django.urls import path
from . import views


urlpatterns = [
    path('allproduct/', views.get_products,name='all_product'),
    path('<int:category_id>/', views.get_bycategory),
    path('<str:product_title>/', views.get_byproduct),
    path('<int:pk>/delete_product/<int:seller_id>/', views.delete,name='delete_product'),
    path('<int:pk>/edit_product', views.edit,name='edit_product'),

]
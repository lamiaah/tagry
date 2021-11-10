from django.urls import path
from . import views


urlpatterns = [
    path('allproduct/', views.get_products,name='all_product'),
    path('<int:category_id>/', views.get_bycategory),
    path('<str:product_title>/', views.get_byproduct),
    path('<int:pk>/edit_product/<int:seller>/', views.edit,name='edit_product'),
    path('<int:pk>/delete_product/<int:seller>/', views.delete,name='delete_product'),
    path('<int:pk>/', views.product_details, name='product_details'),

]
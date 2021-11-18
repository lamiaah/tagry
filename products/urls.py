from django.urls import path
from . import views


urlpatterns = [
    path('allproduct/', views.get_products,name='all_product'),
    path('<int:pk>/edit_product/<int:seller>/', views.edit,name='edit_product'),
    path('<int:pk>/delete_product/<int:seller>/', views.delete,name='delete_product'),
    path('product_details/<int:pk>/', views.product_details, name='product_details'),
    path('product_add/<int:pk>/', views.post_product, name='product_add'),

]
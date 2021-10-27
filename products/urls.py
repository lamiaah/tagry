from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_products),
    path('<int:category_id>/', views.get_bycategory),
    path('<str:product_title>/', views.get_byproduct),

]
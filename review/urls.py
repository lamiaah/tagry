from django.urls import path
from . views import ReviewProduct

urlpatterns = [
    
    path('<int:products_id>/', ReviewProduct.as_view())
    ]
from django.urls import path 
from .import views 



urlpatterns = [
    path('cate_list', views.category_list ,name='home'),
    path('add/',views.post,name='addcate'),
    path('cate/<int:pk>/delete',views.delete,name='delete'),
  
]


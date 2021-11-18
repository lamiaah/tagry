from django.urls import path
from .import views 


urlpatterns = [
    
    path('all_stores',views.stores_view ,name= 'stores'),
    path('add_stores<int:pk>/',views.add_stores ,name= 'add_stores'),

    path('edit_stores/<int:stores_id>/<int:seller>/', views.edit_stores ,name= 'edit_stores'),
    path('delete_stores/<int:pk>/<int:seller>/', views.delete ,name= 'delete_stores'),
    
]
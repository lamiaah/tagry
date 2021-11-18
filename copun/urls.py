from django.urls import path
from .import views 


urlpatterns = [
    path('all_conpun',views.copun_view ,name= 'copun'),
    path('add_copun',views.add_copun ,name= 'add_copun'),
    path('edit_copun<int:copun_id>', views.eidt_copun ,name= 'edit_copun'),
    path('delete_copun<int:pk>', views.delete ,name= 'delete_copun'),
    
]
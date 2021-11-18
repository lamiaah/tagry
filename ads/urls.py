from django.urls import path
from .import views 


urlpatterns = [
    path('all_ads',views.ads_view ,name= 'ads'),
    path('add_ads',views.add_ads ,name= 'add_ads'),
    path('edit_ads<int:ads_id>', views.eidt_ads ,name= 'edit_ads'),
    
]
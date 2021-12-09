
from django.urls import path
from ads.Api.views import AdsAdd, AdsList, PutAds

urlpatterns = [
    path('all_ads/', AdsList.as_view()),
    path('add/',AdsAdd.as_view()),
    
    path('put/<int:id>/',PutAds.as_view()),
    path('delete/<int:id>/',PutAds.as_view()),
]
from  django.urls import path
from categories.Api.views import CategoryApiList 

urlpatterns = [
    path ('all/',CategoryApiList.as_view()),
 
]



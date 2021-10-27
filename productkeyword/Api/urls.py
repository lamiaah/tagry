from django.urls import path
from productkeyword.Api.views import AddKey  ,KeyWprdList

urlpatterns = [
    path('add/',AddKey.as_view()),
    path('all/',KeyWprdList.as_view()),
 ]
 
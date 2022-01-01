
from django.urls import path
from users.Api.views import  UserLogout,UpdateUserPassword 

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  
    path('userLogout', UserLogout.as_view()),
    
    path('updatePassword/<int:user_id>', UpdateUserPassword.as_view())
]
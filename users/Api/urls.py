
from django.urls import path
from users.Api.views import  UserrLogout
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  
    path('userLogout', UserrLogout.as_view()),
    
    # path('updatePassword/<int:user_id>', UpdateUserPassword.as_view())
]
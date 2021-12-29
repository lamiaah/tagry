
from django.urls import path
from users.Api.views import UserLogin, UserLogout, UserData, UpdateUserPassword ,RegisterView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('userLogin', UserLogin.as_view()),
    path('reister/',RegisterView.as_view()),
    path('userLogout', UserLogout.as_view()),
    path('userData/<int:pk>', UserData.as_view()),
    path('updatePassword/<int:pk>', UpdateUserPassword.as_view())
]
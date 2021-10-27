from  django.urls import path
from noti.Api.views import  NotiApiList

urlpatterns = [
    path ('noti/<int:user>/',NotiApiList.as_view()),
]

from  django.urls import path
from area.Api.views import AreaApiList

urlpatterns = [
    path ('all/',AreaApiList.as_view()),
]

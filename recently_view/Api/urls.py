from django.urls import path
from  recently_view.Api.views import RecentlyViewApiList ,AddRvie


urlpatterns = [
    path('recently/<int:user_id>/',RecentlyViewApiList.as_view()),
    path('add/',AddRvie.as_view()),
]

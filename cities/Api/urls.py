from  django.urls import path
from cities.Api.views import CitiesApiList

urlpatterns = [
    path ('',CitiesApiList.as_views()),
]

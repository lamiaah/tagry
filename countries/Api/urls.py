from  django.urls import path
from countries.Api.views import CountriesApiList

urlpatterns = [
    path ('',CountriesApiList.as_view())
]
from django.urls import path
from seller_user.Api.views import RegisterSeller


urlpatterns = [
    path('register', RegisterSeller.as_view())
]

# from  django.urls import path
# from seller_user.Api.views import SellerApiList ,AddInfo ,UpdateInfo

# urlpatterns = [
#     path ('seller/',SellerApiList.as_view()),
#     path ('add/', AddInfo.as_view()),
#     path ('put/<int:id>/', UpdateInfo.as_view()),
# ]

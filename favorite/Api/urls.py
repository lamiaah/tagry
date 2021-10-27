from django.urls import path
from favorite.Api.views import FavoriteApiList ,PostProduct,Delete


urlpatterns = [
    path('all/<int:users_id>/',FavoriteApiList.as_view()),
    path('add/',PostProduct.as_view()),
    path('delete/<int:id>/',Delete.as_view()),

]

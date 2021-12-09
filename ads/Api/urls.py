
from django.urls import path
from ads.Api.views import AdsAdd, AdsList

urlpatterns = [
    path('all_ads/', AdsList.as_view()),
    path('add/',AdsAdd.as_view()),
    # path('review_product/<int:product_id>/', ReviewProductList.as_view()),
    # path('put/<int:id>/',PutReview.as_view()),
    # path('delete/<int:id>/',PutReview.as_view()),
]
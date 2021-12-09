
from django.urls import path
from review.Api.views import ReviewApiList , ReviewProductList ,ReivewView  ,PutReview


urlpatterns = [
    path('review/<int:user_id>/', ReviewApiList.as_view()),
    path('add/',ReivewView.as_view()),
    path('review_product/<int:product_id>/', ReviewProductList.as_view()),
    path('put/<int:id>/',PutReview.as_view()),
    path('delete/<int:id>/',PutReview.as_view()),
    

    
]

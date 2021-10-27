from  django.urls import path
from offers.Api.views import   OfferApiList ,PostOffer ,UpdatOffer

urlpatterns = [
    path ('all/',  OfferApiList.as_view()),
    path ('add/',  PostOffer.as_view()),
    path ('put/<int:id>/', UpdatOffer.as_view()),
]

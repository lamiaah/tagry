from django.urls import path
from languages.Api.views import LanguageList
urlpatterns = [
    path('all/', LanguageList.as_view()),
]

from django.urls import path
from .  import views

urlpatterns = [
    path('all/<int:users_id>/', views.get_fav)
    ]
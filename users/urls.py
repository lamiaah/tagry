from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.register , name="register"),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('users_list/', views.users , name='users_list'),
    path('user_detail/<int:pk>', views.user_details , name='user_detail'),
    path('logout/', views.logout, name='logout'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('new_user/', views.new_user, name='new_user') 
]

from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.register , name="register"),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('users_list/', views.users , name='users_list'),
    path('logout/', views.logout, name='logout')  ,
    path('delete/<int:pk>', views.delete_user, name='delete') 
]

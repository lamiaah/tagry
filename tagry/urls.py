"""tagry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from languages import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views




urlpatterns = [
    path('admin/', admin.site.urls  ),
    path('', views.home_view , name= 'base'),
    path('user/',include('users.urls')),
    path('cate/', include('categories.urls')),
    path('area/', include('area.urls')),
    path('city/', include('cities.urls')),
    path('country/', include('countries.urls')),
    path('favorite/', include('favorite.urls')),
    path('not/', include('noti.urls')),
    path('offers/', include('offers.urls')),
    path('product/', include('products.urls')),
    path('purchase/', include('purchase.urls')),
    path('recently/', include('recently_view.urls')),
    path('review/', include('review.urls')),
    path('seller/', include('seller_user.urls',namespace='seller_user')),
    path('shopping_cart/', include('shopping_cart.urls')),
    path('languages/',include('languages.urls')),
    path('key/',include('productkeyword.urls')),
    path('buyer/',include('buyer.urls')),
    #api
    path('api/buyer/',include('buyer.Api.urls')),
    path('api/language/',include('languages.Api.urls')),
    path('api/category/',include('categories.Api.urls')),
    path('api/offer/',include('offers.Api.urls')),
    path('api/product/',include('products.Api.urls')),
    path('api/seller/',include('seller_user.Api.urls')),
    path('api/shoppingcart/',include('shopping_cart.Api.urls')),
    path('api/purchase/',include('purchase.Api.urls')),
    path('api/favorite/',include('favorite.Api.urls')),
    path('api/recently/',include('recently_view.Api.urls')),
    path('api/review/',include('review.Api.urls')),
    path('api/noti/',include('noti.Api.urls')),
    path('api/user/',include('users.Api.urls')),
    #path('api/popular/',include('popular.Api.urls')),
    path('api/keyword/',include('productkeyword.Api.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 

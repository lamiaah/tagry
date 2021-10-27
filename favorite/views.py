from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from favorite.models import Favorite
from django.views.generic import ListView
from django.http import HttpResponse

@login_required(login_url='login')
def get_fav(request, users_id):
    if request.user.is_authenticated == True:
        product = Favorite.objects.filter(users_id= users_id)
        return HttpResponse(product)
    else: 
        return redirect ('login')     


   



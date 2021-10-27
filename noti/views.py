from django.shortcuts import redirect, render
from noti.models import Noti
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url='lohin')
def get_noti( request, user_id):
    if request.user.is_authenticated == True:
        x = Noti.objects.filter(user_id=user_id)
        return HttpResponse(x)
    else:
        return redirect('login')




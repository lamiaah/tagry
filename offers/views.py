
from django.shortcuts import redirect
from offers.models import Offers
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def get(self ,request ):
    if request.user.is_authenticated == True:

        offer = Offers.objects.all()
        return HttpResponse(offer)
    else:
        return redirect('login')    
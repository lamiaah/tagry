from django.shortcuts import redirect, render
from recently_view.models import Recently_view
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
    
def get_recently_view(self, request, user_id):
    if request.user.is_authenticated == True:
        recently = Recently_view.objects.filter(user_id=user_id)
        return HttpResponse(recently)
    else:
        return redirect ('login')


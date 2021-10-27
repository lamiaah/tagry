
from django.http import HttpResponse
from django.shortcuts import redirect, render
from shopping_cart.models import Shopping_cart
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def get_shopping_cart(self, request, user_id):
    if request.user.is_authenticated == True:
        shopping = Shopping_cart.objects.filter(user_id=user_id)
        return HttpResponse(shopping)
    else:
        return redirect('login')    
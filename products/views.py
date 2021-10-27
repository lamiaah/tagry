from django.shortcuts import redirect, render
from products.models import Products
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def get_products(self, request):
    if request.user.is_authenticated == True:
        product = Products.objects.all()
        return HttpResponse(product)
    else:
        return redirect('login')    




@login_required(login_url='login')
def get_bycategory(self, request, category_id):
    if request.user.is_authenticated == True:
        product = Products.objects.filter(category_id=category_id)
        return HttpResponse(product)
    else:
        return redirect('login')

@login_required(login_url='login')
def get_byproduct(self, request, product_title):
    if request.user.is_authenticated == True:
        product = Products.objects.filter( product_title=product_title)
        return HttpResponse(product)
    else: 
        return redirect('login')


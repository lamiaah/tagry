from datetime import date
from django.shortcuts import redirect, render
from products.models import Products ,ProductImage
from.forms import  ProductForm ,ImageForm
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# def image(products):
#     for product in products:
#         image = ProductImage.objects.filter(product_id=product["id"])
#         image_form = ImageForm(request.POST)
#         if image_form.is_valid():


@login_required(login_url='login')
def get_products(request):
    if request.user.is_authenticated == True:
        product = Products.objects.filter(is_archived=False)
        image = ProductImage.objects.filter(product = product)
        context ={
            'product':product,
            'image':image,
        }
        return render(request,'product/products.html',context)
    else:
        return redirect('login')    




@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.created_by =request.user
                form.instance.updated_by =request.user

                form.save()
                return redirect('')
            else: 
                print(form.errors.as_data()) 
                return render(request,'categories/category_add.html',{'form':form})
        else:
            form = ProductForm()
        return render(request,'categories/category_add.html',{'form':form})
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


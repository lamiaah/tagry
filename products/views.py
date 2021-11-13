from datetime import date
from django.shortcuts import redirect, render ,get_object_or_404
from django.urls.base import reverse
from products.models import Products ,ProductImage
from seller_user.models import Seller
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
        if request.user.is_superuser:
            product = Products.objects.filter(is_archived=False)
            image = ProductImage.objects.filter(product = product)
            context ={
                'product':product,
                'image':image,
            }
            return render(request,'product/products.html',context)
        else:
           return redirect('login')      
    else:
        return redirect('login')    




@login_required(login_url='login')
def post_product(request,pk):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            seller = Seller.objects.get(pk=pk)
            if request.method == 'POST':
                Productform = ProductForm(request.POST, request.FILES)
                Imageform = ImageForm(request.POST, request.FILES)
                if Productform.is_valid() and Imageform.is_valid() :
                    Productform.instance.created_user =request.user
                    Productform.instance.updated_user =request.user
                    Productform.instance.seller_id = seller
                    Productform.save()
                    product = Productform.instance
                    Imageform.instance.product_id =product.id
                    Imageform.save()
                    return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))
                else: 
                    #print(form.errors.as_data()) 
                    return render(request,'product/new_product.html',{'Productform':Productform,'Imageform':Imageform})    
            else:
                Productform = ProductForm()
                Imageform = ImageForm()
            return render(request,'product/new_product.html',{'Productform':Productform,'Imageform':Imageform})
        else:
            return redirect('login')     
    else:
        return redirect('login')


@login_required(login_url='login')  
def delete(request ,pk ,seller):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            product = Products.objects.get(pk=pk)
            template_name  ='product/delete_pro.html'  
            if request.method == "POST":
                product.is_archived = True
                product.save()
                return redirect(reverse('seller_user:seller_detail' ,args=(seller,)))
            context = {'product':product}
            return render(request, template_name, context) 
        else:
           return redirect('login')
    else:
      return redirect('login')


@login_required(login_url='login')
def edit(request ,pk ,seller ):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            Product = Products.objects.get(pk=pk)
            seller = Seller.objects.get(pk=seller)
            Imageform = ImageForm(request.POST, request.FILES)
            productform = ProductForm(request.POST ,request.FILES , instance= Product)
            if request.method == 'POST':
                if Imageform.is_valid() and  productform.is_valid() :
                    productform.instance.created_user =request.user
                    productform.instance.updated_user =request.user
                    productform.instance.seller_id = seller
                    productform.save()
                    product = productform.instance
                    Imageform.instance.product_id =product.id
                    Imageform.save()
                    return redirect(reverse('seller_user:seller_detail' ,args=(seller,)))
                else:
                   
                    return render(request,'product/product_edit.html',{'productform':productform,'Imageform':Imageform})   
            else:
                productform = ProductForm()
                Imageform = ImageForm()
            return render(request,'product/product_edit.html',{'productform':productform,'Imageform':Imageform})
        else:
           return redirect('login')
    else:
      return redirect('login')        



@login_required(login_url='login')
def product_details(request, pk):
    if request.user.is_authenticated :
       if request.user.is_superuser:
            product_data = Products.objects.get(pk = pk)
            image = ProductImage.objects.filter(product = product_data)
            context = {
                'product_data' : product_data,
                'image':image
            }
            return render(request, 'product/product_detail.html', context)
       else:
            return redirect('login')
    else:
        return redirect('login')      




# @login_required(login_url='login')
# def get_bycategory(self, request, category_id):
#     if request.user.is_authenticated == True:
#         product = Products.objects.filter(category_id=category_id)
#         return HttpResponse(product)
#     else:
#         return redirect('login')

# @login_required(login_url='login')
# def get_byproduct(self, request, product_title):
#     if request.user.is_authenticated == True:
#         product = Products.objects.filter( product_title=product_title)
#         return HttpResponse(product)
#     else: 
#         return redirect('login')


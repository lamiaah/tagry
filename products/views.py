from datetime import date
from django.shortcuts import redirect, render ,get_object_or_404
from django.urls.base import reverse
from products.models import Products ,Images
from seller_user.models import Seller
from.forms import  ProductForm ,ImageForm
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def get_products(request):
    if request.user.is_authenticated == True:
        if request.user.is_superuser:
            product = Products.objects.filter(is_archived=False)
            for i in product:
                image = Images.objects.filter(product = i)
                i.all_images =image
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
def add_product(request ,pk):
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        seller = Seller.objects.get(pk=pk)
        if request.method =='POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.instance.created_user =request.user
                form.instance.updated_user =request.user
                form.instance.seller_id = seller
                x= form.save()
                for i in request.FILES.getlist('img'):
                    image_form = ImageForm(request.POST ,request.FILES)
                    if image_form.is_valid():
                        add_image(x,i)
                return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))  
            
        else:
            form = ProductForm()
            image_form =ImageForm(request.POST, request.FILES)
        return render(request, 'product/new_product.html',{'form':form,'image_form':image_form,})        
        


def add_image(product_id ,img):
    try:
        new_image = Images.objects.create(product =product_id ,image=img )
        new_image.save()
        return new_image
    except Exception as e:
        print(e)
        return False    




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


# @login_required(login_url='login')
# def edit(request ,pk ,seller ):
#     if request.user.is_authenticated ==True :
#         if request.user.is_superuser:
#             Product = Products.objects.get(pk=pk)
#             seller = Seller.objects.get(pk=seller)
#             Imageform = ImageForm(request.POST, request.FILES)
#             productform = ProductForm(request.POST ,request.FILES , instance= Product)
#             if request.method == 'POST':
#                 if Imageform.is_valid() and  productform.is_valid() :
#                     productform.instance.created_user =request.user
#                     productform.instance.updated_user =request.user
#                     productform.instance.seller_id = seller
#                     productform.save()
#                     product = productform.instance
#                     Imageform.instance.product_id =product.id
#                     Imageform.save()
#                     return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))
#                 else:
                   
#                     return render(request,'product/product_edit.html',{'productform':productform,'Imageform':Imageform})   
#             else:
#                 productform = ProductForm(instance= Product)
#                 Imageform = ImageForm()
#             return render(request,'product/product_edit.html',{'productform':productform,'Imageform':Imageform})
#         else:
#            return redirect('login')
#     else:
#       return redirect('login')        


@login_required(login_url='login') 
def edit_product(request ,pk,seller):
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        seller = Seller.objects.get(pk=seller)
        product = Products.objects.get(pk=pk)
        image = Images.objects.filter(product = product)
        product.all_images =image
        if request.method =='POST':
            form = ProductForm(request.POST,instance= product)
            if form.is_valid():
                form.instance.created_user =request.user
                form.instance.updated_user =request.user
                form.instance.seller_id = seller
                x= form.save()
                for i in request.FILES.getlist('img'):
                    image_form = ImageForm(request.POST ,request.FILES ,instance=image)
                    if image_form.is_valid():
                        add_image(x,i)
                return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))  
            
        else:
            form = ProductForm(instance= product)
            image_form =ImageForm(request.POST ,request.FILES ,instance=image)
        return render(request, 'product/product_edit.html',{'form':form,'image_form':image_form,}) 



@login_required(login_url='login')
def product_details(request, pk):
    if request.user.is_authenticated :
       if request.user.is_superuser:
            product_data = Products.objects.get(pk = pk)
            image = Images.objects.filter(product = product_data)
            product_data.all_images =image
            context = {
                'product_data' : product_data,
                'image':image
            }
            return render(request, 'product/product_detail.html', context)
       else:
            return redirect('login')
    else:
        return redirect('login')      





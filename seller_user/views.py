from django.db.models import query_utils
from django.http.response import Http404
from products.models import Products , Images
from django.shortcuts import render ,redirect ,get_object_or_404
from seller_user.models import Seller
from stores.models import SellerStores
from.forms import  SellerForm ,RegisterForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

@login_required(login_url='login')
def seller(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            seller = Seller.objects.filter(is_archive=False)
            context = {
                'seller':seller  
            }
            return render(request,'seller/seller.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')


@login_required(login_url='login')
def seller_details(request, pk):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            seller_data = Seller.objects.get(pk = pk)
            seller_products = Products.objects.filter(seller_id = pk ,is_archived=False or None)  
            for i in seller_products:
                image = Images.objects.filter(product = i or None)
                
                i.all_images= image
            stores = SellerStores.objects.filter(seller=pk,is_archived=False)
            context = {
                'seller_data' : seller_data,
                'seller_products' :seller_products,
                'stores':stores ,
                'images':i.all_images
            }
            return render(request, 'seller/seller_detail.html', context)
        else:
            return redirect('login')
    else:
        return redirect('login')

@login_required(login_url='login')
def seller_regieter(request ):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.instance

                    return redirect(reverse('seller_user:add_seller',args=(user.id,)))
                else:
                    return render(request ,'seller/register_seller.html',{'form':form})      
            else:
                form = RegisterForm()
            return render(request,'seller/register_seller.html',{'form':form })    
        else:
           return redirect('login')
    else:
      return redirect('login')

@login_required(login_url='login')
def post(request ,pk):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            user =CustomUser.objects.get(pk = pk)
            if request.method == 'POST':
                form = SellerForm(request.POST, request.FILES or None)
                if form.is_valid():
                    form .instance.user = user
                    form.save()
                    print(form.data)
                    return redirect('seller_user:seller_list')
                else: 
                    print(form.errors.as_data()) 
                    return render(request,'seller/newseller.html',{'form':form})  
            else:
                form = SellerForm()
            return render(request,'seller/newseller.html',{'form':form})    
        else:
           return redirect('login')

    else:
        return redirect('login')
   
@login_required(login_url='login')  
def delete(request ,pk):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            seller = Seller.objects.get(pk=pk)
            template_name  ='seller/seller_delete.html'  
            if request.method == "POST":
                seller.is_archive = True
                seller.save()
                return redirect('seller_user:seller_list')
            context = {'seller':seller}
            return render(request, template_name, context)  
        else:
           return redirect('login')

    else:
        return redirect('login')    



@login_required(login_url='login')
def edit(request ,pk):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            seller = get_object_or_404(Seller ,pk=pk)
            form = SellerForm(request.POST ,request.FILES , instance= seller)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return redirect('seller_user:seller_list')
                else:
                    print(form.errors.as_data()) 
                    return render(request,'seller/seller_edit.html',{'form':form})   
            else:
                form = SellerForm(instance= seller)
            return render(request,'seller/seller_edit.html',{'form':form})
        else:
           return redirect('login')
    else:
      return redirect('login')        



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        product = Products.objects.filter(product_title__icontains=q)
        return render(request, 'seller/product_search.html', {'product': product, 'query': q})
    else:
        return print('Please submit a search term.')

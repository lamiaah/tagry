from django.db.models import query_utils
from django.http.response import Http404
from products.models import Products , ProductImage
from django.shortcuts import render ,redirect ,get_object_or_404
from seller_user.models import Seller
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
            seller_products = Products.objects.filter(seller_id = pk ,is_archived=False)
            image = ProductImage.objects.filter(product = seller_products)
            context = {
                'seller_data' : seller_data,
                'seller_products' :seller_products,
                'image':image
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
                    return redirect('seller_user:seller_list')
                else:
                    print(form.errors.as_data()) 
                    return render(request,'seller/seller_edit.html',{'form':form})   
            else:
                form = SellerForm()
            return render(request,'seller/seller_edit.html',{'form':form})
        else:
           return redirect('login')
    else:
      return redirect('login')        



def search_product(request):
    if request.method == "POST":
        query_name = request.POST.get('product_title', None)
        if query_name:
            results = Products.objects.filter(product_title__contains=query_name)
            return render(request, 'seller/seller.html', {"results":results})

    return render(request, 'seller/seller.html')


from typing import Reversible
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls.base import reverse
from seller_user.models import Seller
from stores.forms import StoresForm, EditStoresForm
from stores.models import SellerStores


@login_required(login_url='login')
def stores_view(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            stores = SellerStores.objects.all()
            context = {
                'stores':stores,
            }
            return render(request,'stores.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')



@login_required(login_url='login')
def add_stores(request,pk):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        seller = Seller.objects.get(pk=pk)
        if request.method == 'POST':
            form = StoresForm(request.POST)
            if form.is_valid():
                form.instance.seller = seller
                form.save()
                return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))
        else:
            form = StoresForm()

        return render(request, 'add_stores.html', {'form' : form})


@login_required(login_url='login')
def edit_stores(request, stores_id,seller):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        seller = Seller.objects.get(pk=seller)

        stores = SellerStores.objects.get(id = stores_id)
        if request.method == 'POST':
            form = EditStoresForm(request.POST, instance= stores)
            form.instance.seller = seller
            if form.is_valid():
                form.save()
                return redirect(reverse('seller_user:seller_detail' ,args=(seller.id,)))
        else:
            form = EditStoresForm(instance= stores)

        return render(request, 'edit_stores.html', {'form' : form})

@login_required(login_url='login')
def delete_store(request ,pk,seller):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            stores = SellerStores.objects.get(pk=pk)
            template_name  ='delete_stores.html'  
            if request.method == "POST":
                stores.is_archived = True
                stores.save()
                return redirect(reverse('seller_user:seller_detail' ,args=(seller,)))
            context = {"stores": stores}
            return render(request, template_name, context)  
        else:
           return redirect('login')    
    else:
        return redirect('login')       
from django.http.response import Http404
from products.models import Products
from django.shortcuts import render ,redirect ,get_object_or_404
from buyer.models import Buyer
from.forms import  BuyerForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def buyer(request):
    if request.user.is_authenticated :
        buyer = Buyer.objects.filter(is_archive=False)
        context = {
            'buyer':buyer  
        }
        return render(request,'buyer/buyer.html',context)
    else:
        return redirect('login')


@login_required(login_url='login')
def buyer_details(request, pk):
    if request.user.is_authenticated :
        buyer_data = Buyer.objects.get(pk = pk)
        context = {
            'buyer_data' : buyer_data,
        }

        return render(request, 'buyer/buyer_detail.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = BuyerForm(request.POST, request.FILES or None)
            if form.is_valid():
                form.save()
                print(form.data)
                return redirect('buyer_list')
            else: 
                print(form.errors.as_data()) 
                return render(request,'buyer/newbuyer.html',{'form':form})  
        else:
            form = BuyerForm()
        return render(request,'buyer/newbuyer.html',{'form':form})    
    else:
        return redirect('login')
   
@login_required(login_url='login')  
def delete(request ,pk):
    if request.user.is_authenticated :
        buyer = Buyer.objects.get(pk=pk)
        template_name  ='buyer/buyer_delete.html'  
        if request.method == "POST":
            buyer.is_archive = True
            buyer.save()
            return redirect('buyer_list')
        context = {'buyer':buyer}
        return render(request, template_name, context)  
    else:
        return redirect('login')    

@login_required(login_url='login')
def edit(request ,pk):
    if request.user.is_authenticated ==True :
        buyer = get_object_or_404(Buyer ,pk=pk)
        form = BuyerForm(request.POST ,request.FILES , instance= buyer)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('buyer_list')
            else:
                print(form.errors.as_data()) 
                return render(request,'buyer/edit_buyer.html',{'form':form})   
        else:
            form = BuyerForm()
        return render(request,'buyer/edit_buyer.html',{'form':form})
    else:
      return redirect('login')
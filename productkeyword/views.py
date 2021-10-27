
from productkeyword.models import Product_keyword
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from.forms import  KeyForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def area_list(request):
    if request.user.is_authenticated:
        key = Product_keyword.objects.all()
        context ={'key': key}
        return render (request ,'key/key.html',context)
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.method == 'POST':
            form = KeyForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.created_user =request.user
                form.instance.updated_user =request.user
                form.save()
                return redirect('key')
            else: 
                print(form.errors.as_data()) 
                return render(request,'key/key_add.html',{'form':form})
        else:
            form = KeyForm()
        return render(request,'key/key_add.html',{'form':form})
    else:
        return redirect('login')

from django.shortcuts import render ,redirect
from.forms import RegisterForm ,NewUserForm ,ChangePassForm
from users.models import CustomUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from seller_user.models import Seller
from buyer.models import Buyer

@login_required(login_url='login')
def users(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            users = CustomUser.objects.filter(is_active= True)
            context={'users':users }
            return render (request ,'user/user_list.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')

@login_required(login_url='login')
def register(request):
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request,'user/register.html',{'form':form})    

   
def logout(request):
    auth.logout(request)
    return redirect('login')



@login_required(login_url='login')  
def delete_user(request ,pk):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            users = CustomUser.objects.get(pk=pk)
            template_name  ='user/delete_user.html'  
            if request.method == "POST":
                users.is_active = False
                users.save()
                return redirect('users_list')
            context = {'users':users}
            return render(request, template_name, context)  
        else:
            return redirect('login')
    else:
        return redirect('login')    


@login_required(login_url='login')  
def new_user(request ):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            template_name  ='user/add_user.html'  
            if request.method == "POST":
                newform = NewUserForm(request.POST)
                if newform.is_valid():
                    newform.save()
                    return redirect('users_list')
                return render(request, template_name, {'newform':newform})  
            else:
                newform = NewUserForm()
            return render(request, template_name, {'newform':newform})          
        else:
            return redirect('login')
    else:
        return redirect('login')    

@login_required(login_url='login')
def edit(request ,pk):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            user = CustomUser.objects.get(pk=pk)
            form = ChangePassForm(request.POST ,request.FILES , instance= user)
            if request.method == 'POST':
                if form.is_valid():
                    return redirect('users_list')
                else:
                    print(form.errors.as_data()) 
                    return render(request,'user/change_pass.html',{'form':form})   
            else:
                form = ChangePassForm(instance= user)
            return render(request,'user/change_pass.html',{'form':form})
        else:
           return redirect('login')
    else:
      return redirect('login')  

@login_required(login_url='login')
def user_details(request, pk):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            user_data =  CustomUser.objects.get(pk = pk)
            context = {
                'user_data' : user_data,
            }
            return render(request, 'user/user_detail.html', context)
        else:
            return redirect('login')
    else:
        return redirect('login')

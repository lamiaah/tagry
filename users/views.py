from django.shortcuts import render ,redirect
from.forms import RegisterForm ,NewUserForm
from users.models import CustomUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def users(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            users = CustomUser.objects.all()
            context={'users':users }
            return render (request ,'user/user_list.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')


def register(request):
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
                users.is_archive = True
                users.save()
                return redirect('user_list')
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
                form = NewUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('user_list')
                return render(request, template_name, {'form':form})  
            else:
                form = NewUserForm()
            return render(request, template_name, {'form':form})          
        else:
            return redirect('login')
    else:
        return redirect('login')    

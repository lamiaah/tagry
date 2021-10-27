from django.shortcuts import render ,redirect
from.forms import RegisterForm
from users.models import CustomUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def users(request):
    if request.user.is_authenticated :
        users = CustomUser.objects.all()
        context={'users':users }
        return render (request ,'user/user_list.html',context)
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


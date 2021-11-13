from area.models import Area
from django.contrib.auth.decorators import login_required
from categories.models import Categories
from django.shortcuts import render ,redirect
from.forms import  AreaForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def area_list(request):
    if request.user.is_authenticated==True:
        if request.user.is_superuser:
            area = Area.objects.all()
            context ={'area': area}
            return render (request ,'area/area.html',context)
        else:
          return redirect('login')          
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
       if request.user.is_superuser:
            if request.method == 'POST':
                form = AreaForm(request.POST, request.FILES)
                if form.is_valid():
                    form.instance.area_created_user =request.user
                    form.instance.area_updated_user =request.user
                    form.save()
                    return redirect('area')
                else: 
                    print(form.errors.as_data()) 
                    return render(request,'area/add_area.html',{'form':form})
            else:
                form = AreaForm()
            return render(request,'area/add_area.html',{'form':form})
       else:
            return redirect('login')    
    else:
        return redirect('login')

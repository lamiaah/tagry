from django.contrib.auth.decorators import login_required
from cities.models import Cities
from django.shortcuts import render ,redirect
from.forms import  CityForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def city_list(request):
    if request.user.is_authenticated:
        city = Cities.objects.all()
        context ={'city': city}
        return render (request ,'city/cities.html',context)
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.method == 'POST':
            form = CityForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.city_created_user =request.user
                form.instance.city_updated_user =request.user
                form.save()
                return redirect('city')
            else: 
                print(form.errors.as_data()) 
                return render(request,'city/city_add.html',{'form':form})
        else:
            form = CityForm()
        return render(request,'city/city_add.html',{'form':form})
    else:
        return redirect('login')
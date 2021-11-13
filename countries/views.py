from  countries.models import Countries
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from.forms import  CountryForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def area_list(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            country = Countries.objects.all()
            context ={'country': country}
            return render (request ,'country/country.html',context)
        else:
           return redirect('login')    
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            if request.method == 'POST':
                form = CountryForm(request.POST, request.FILES)
                if form.is_valid():
                    form.instance.country_created_user =request.user
                    form.instance.country_updated_user =request.user
                    form.save()
                    return redirect('country')
                else: 
                    print(form.errors.as_data()) 
                    return render(request,'country/country_add.html',{'form':form})
            else:
                form = CountryForm()
            return render(request,'country/country_add.html',{'form':form})
        else:
            return redirect('login')
    else:
        return redirect('login')
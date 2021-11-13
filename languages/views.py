from  languages.models import Languages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from.forms import  LanguagesForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def lan_list(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            lan = Languages.objects.all()
            context ={'lan': lan}
            return render (request ,'languages/languages.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            if request.method == 'POST':
                form = LanguagesForm(request.POST, request.FILES)
                if form.is_valid():
                    form.instance.created_user =request.user
                    form.instance.updated_user =request.user
                    form.save()
                    return redirect('languages')
                else: 
                    print(form.errors.as_data()) 
                    return render(request,'languages/languages_add.html',{'form':form})
            else:
                form = LanguagesForm()
            return render(request,'languages/languages_add.html',{'form':form})
        else:
           return redirect('login')
    else:
        return redirect('login')
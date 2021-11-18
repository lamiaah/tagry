from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ads.form import AddAdsForm, EditAdsForm
from ads.models import Ads


@login_required(login_url='login')
def ads_view(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            ads = Ads.objects.all()
            context = {
                'ads':ads,
                'ads_counter' : len(ads)
            }
            return render(request,'ads_view.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')



@login_required(login_url='login')
def add_ads(request):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = AddAdsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('ads')
        else:
            form = AddAdsForm()

        return render(request, 'add_ads.html', {'form' : form})


@login_required(login_url='login')
def eidt_ads(request, ads_id):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        ads = Ads.objects.get(id = ads_id)
        if request.method == 'POST':
            form = EditAdsForm(request.POST, instance= ads)
            if form.is_valid():
                form.save()
                return redirect('ads')
        else:
            form = EditAdsForm(instance= ads)

        return render(request, 'edit_ads.html', {'form' : form})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from copun.forms import CopunForm, EditCopunForm
from copun.models import Copun


@login_required(login_url='login')
def copun_view(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            copun = Copun.objects.all()
            context = {
                'copun':copun,
            }
            return render(request,'copun_view.html',context)
        else:
            return redirect('login')
    else:
        return redirect('login')



@login_required(login_url='login')
def add_copun(request):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = CopunForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('copun')
        else:
            form = CopunForm()

        return render(request, 'add_copun.html', {'form' : form})


@login_required(login_url='login')
def eidt_copun(request, copun_id):
    
    if request.user.is_superuser == False:
        return redirect('login')
    else:
        copun = Copun.objects.get(id = copun_id)
        if request.method == 'POST':
            form = EditCopunForm(request.POST, instance= copun)
            if form.is_valid():
                form.save()
                return redirect('copun')
        else:
            form = EditCopunForm(instance= copun)

        return render(request, 'edit_copun.html', {'form' : form})

@login_required(login_url='login')
def delete(request ,pk):
    if request.user.is_authenticated ==True :
        if request.user.is_superuser:
            copun = Copun.objects.get(pk=pk)
            template_name  ='delete_copun.html'  
            if request.method == "POST":
                copun.is_archive = True
                copun.save()
                return redirect('copun')
            context = {"copun": copun}
            return render(request, template_name, context)  
        else:
           return redirect('login')    
    else:
        return redirect('login')       
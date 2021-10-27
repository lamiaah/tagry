
from django.contrib.auth.decorators import login_required
from categories.models import Categories
from django.shortcuts import render ,redirect
from.forms import  CategoryForm



@login_required(login_url='login')
def category_list(request):
    if request.user.is_authenticated:
        category = Categories.objects.filter(is_archive =False)
        context ={'cate':category }
        return render (request ,'categories/categories.html',context)
    else:
        return redirect('login')


@login_required(login_url='login')
def post(request):
    if request.user.is_authenticated ==True :
        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.created_by =request.user
                form.instance.updated_by =request.user
                form.save()
                return redirect('home')
            else: 
                print(form.errors.as_data()) 
                return render(request,'categories/category_add.html',{'form':form})
        else:
            form = CategoryForm()
        return render(request,'categories/category_add.html',{'form':form})
    else:
        return redirect('login')


def delete(request ,pk):
    cate = Categories.objects.get(pk=pk)
    template_name  ='categories/category_delete.html'  
    if request.method == "POST":
        cate.is_archive = True
        cate.save()
        return redirect('home')
    context = {"cate": cate}
    return render(request, template_name, context)  

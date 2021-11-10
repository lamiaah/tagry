
from django.contrib.auth.decorators import login_required
from categories.models import Categories ,SubCategory
from django.shortcuts import render ,redirect ,get_object_or_404 ,resolve_url 
from django.urls import reverse
from.forms import  CategoryForm ,SubCategoryForm




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

@login_required(login_url='login')
def delete(request ,pk):
    if request.user.is_authenticated ==True :
        cate = Categories.objects.get(pk=pk)
        template_name  ='categories/category_delete.html'  
        if request.method == "POST":
            cate.is_archive = True
            cate.save()
            return redirect('home')
        context = {"cate": cate}
        return render(request, template_name, context)  
    else:
        return redirect('login')


@login_required(login_url='login')
def edit(request ,pk):
    if request.user.is_authenticated ==True :
        cate = get_object_or_404(Categories ,pk=pk)
        form = CategoryForm(request.POST ,request.FILES , instance= cate)
        if request.method == 'POST':
            if form.is_valid():
                form.instance.created_by =request.user
                form.instance.updated_by =request.user
                form.save()
                return redirect('home')
            else:
                print(form.errors.as_data()) 
                return render(request,'categories/category_edit.html',{'form':form})   
        else:
            form = CategoryForm()
        return render(request,'categories/category_edit.html',{'form':form})
    else:
      return redirect('login')

@login_required(login_url='login')
def edit_sub(request ,pk):
    if request.user.is_authenticated ==True :
        subcate = get_object_or_404(SubCategory,pk=pk)
        form = SubCategoryForm(request.POST ,request.FILES , instance= subcate)
        if request.method == 'POST':
            if form.is_valid():
                form.instance.created_by =request.user
                form.instance.updated_by =request.user
                form.save()
                return redirect('home')
            else:
                print(form.errors.as_data()) 
                return render(request,'sub_category/sub_cate_edit.html',{'form':form})   
        else:
            form = CategoryForm()
        return render(request,'sub_category/sub_cate_edit.html',{'form':form})
    else:
      return redirect('login')




@login_required(login_url='login')
def sub_category_list(request ,pk):
    if request.user.is_authenticated:
        sub_category = SubCategory.objects.filter(category_id=pk ,is_archive =False)
        category = Categories.objects.get(pk=pk)
        context ={
            'sub_cate':sub_category ,
            'cate' :category,
        }
        return render (request ,'sub_category/sub_category.html',context)
    else:
        return redirect('login')




@login_required(login_url='login')
def post_sub(request ,cateid):
    if request.user.is_authenticated ==True :
        category = Categories.objects.get(pk=cateid)
        if request.method == 'POST':
            form =SubCategoryForm(request.POST, request.FILES )
            if form.is_valid():
                form.instance.created_by =request.user
                form.instance.updated_by =request.user
                form.instance.category_id = category
                form.save()
                return redirect(reverse('sub_home',args=(category.id)))
            else: 
                print(form.errors.as_data()) 
                return render(request,'sub_category/new_sub.html',{'form':form})
        else:
            form = SubCategoryForm()
        return render(request,'sub_category/new_sub.html',{'form':form})
    else:
        return redirect('login')



def deletesub(request ,pk):
    subcate = SubCategory.objects.get(pk=pk)
    template_name  ='sub_category/sub_cate_delete.html'  
    if request.method == "POST":
        subcate.is_archive = True
        subcate.save()
        return redirect('home')
    context = {"cate": subcate}
    return render(request, template_name, context)  

from django.shortcuts import redirect, render
from review.models import Review
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def get_review(request, pk):
    if request.user.is_authenticated == True:
            review = Review.objects.filter(pk=pk)
            context={'review':review}
            return context
    else:
            return redirect('login')


class ReviewProduct(ListView):

    def get(self, request, products_id):
        review = Review.objects.filter(products_id=products_id)
        return HttpResponse(review)



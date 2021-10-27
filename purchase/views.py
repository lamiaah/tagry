from django.shortcuts import redirect, render
from purchase.models import Purchase
from datetime import date
from django.contrib.auth.decorators import login_required

time_today = date.today()

def get_orders():
   
    orders = Purchase.objects.filter(
        created_at__year= time_today.year,
        created_at__month= time_today.month,
        created_at__day= time_today.day,
    )
    context={
        'orders_len': len(orders),
        'orders' : []
    }
    for i in orders:
        context['orders'].append(i)
    return context



def get_revenue():

    orders = Purchase.objects.filter(
        created_at__year= time_today.year,
        created_at__month= time_today.month,
    )
    get_total_price = []
    for i in orders:
        get_total_price.append(i.shopping_cart_id.total_price)

    context = {
        'total_amount' : sum(get_total_price)
    }

    return context
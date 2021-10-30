from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from purchase.views import get_orders, get_revenue
from users.models import CustomUser
from seller_user.models import Seller
from buyer.models import Buyer

@login_required(login_url='login')
def home_view(request):    
    if request.user.is_authenticated == True:
        orders = get_orders()
        revenue = get_revenue()
        all_users = CustomUser.objects.all(),
        sellers = Seller.objects.all()
        buyer = Buyer.objects.all()
        context = {
            'orders_lens' : orders['orders_len'],
            'orders' : orders['orders'],
            'revenue' : revenue['total_amount'],
            'user' : request.user,
            'users_len' : len(all_users),
            'seller' : len(sellers),
            'buyer' : len(buyer)
        }
        return render(request, 'Templates/admin/base.html', context)
    else:
        return redirect('login')



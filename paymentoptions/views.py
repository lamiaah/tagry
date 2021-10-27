
from django.views.generic import ListView
from paymentoptions.models import PaymentOption
from django.http import HttpResponse

class OptionsListview(ListView):

    def get(self):
        option = PaymentOption.objects.all()
        return HttpResponse(option)
    
    
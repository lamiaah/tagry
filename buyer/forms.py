from django import forms
from buyer.models import Buyer
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class BuyerForm(forms.ModelForm):
    class Meta : 
        model = Buyer
        fields = ['name','about','image','address','country','city','area']



class RegisterForm(UserCreationForm):
  

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
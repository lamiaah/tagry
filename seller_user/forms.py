
from django import forms
from seller_user.models import Seller
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class SellerForm(forms.ModelForm):
    class Meta : 
        model = Seller
        fields = '_all__'
        exclude =('user')
        

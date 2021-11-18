from django import forms
from django.forms.fields import DateField
from copun.models import Copun
from django.conf import settings


class CopunForm(forms.ModelForm):


    class Meta:
        model = Copun
        fields = ['copun_text', 'copun_value', 'copun_status']



class EditCopunForm(forms.ModelForm):

    class Meta:
        model = Copun
        fields = ['copun_text', 'copun_value', 'copun_status']
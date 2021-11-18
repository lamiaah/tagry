from django import forms
from django.forms.fields import DateField
from ads.models import Ads
from django.conf import settings


class AddAdsForm(forms.ModelForm):

    start_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    end_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Ads
        fields = ['product', 'start_date', 'end_date', 'added_by']



class EditAdsForm(forms.ModelForm):

    start_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    end_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Ads
        fields = ['product', 'start_date', 'end_date', 'added_by', 'is_archived']
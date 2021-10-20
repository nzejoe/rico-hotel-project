from django import forms
from django.forms import fields

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'phone',
            'address_1',
            'address_2',
            'city',
            'state',
            'country'
        ]
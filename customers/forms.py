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
        
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address 2'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }
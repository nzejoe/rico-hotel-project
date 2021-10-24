import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Booking

now = datetime.datetime.now() # get the current date

class BookingForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'min': now.date()}), help_text='Pick a date')
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}), label='Number of days')

    class Meta:
        model = Booking
        fields = ['start_date', 'duration']

    def clean(self):
        data = self.cleaned_data
        date = data.get('start_date')
        if now.date() > date:
            raise ValidationError('Invalid date selected')
            
        return super(BookingForm, self).clean()

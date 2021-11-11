import datetime

from django import forms
from django.core.exceptions import ValidationError

# helpers
from utils.bookings import ValidateDate

from .models import Booking


now = datetime.datetime.now()  # get the current date


class BookingForm(forms.ModelForm):
    room_number = forms.CharField(required=False)
    class Meta:
        model = Booking
        fields = ['start_date', 'duration', 'room_number', ]
        labels = {
            'start_date': 'Check in',
            'duration': 'Number of nights',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': now.date().today()}),
            'duration': forms.NumberInput(attrs={'min': 1}),
        }

    def clean(self):
        data = self.cleaned_data
        start_date = data.get('start_date')
        duration = data.get('duration')
        room = data.get('room_number')
        if now.date() > start_date:
            raise ValidationError('Invalid date selected')

        entered_dates = ValidateDate(start_date=start_date, duration=duration, room_number=room)

        if entered_dates.not_valid():
            # self._errors['start_date'] = self.error_class(
            #     [f'{entered_dates.error_date} has already been booked for this room!'])
            raise ValidationError(f'{entered_dates.error_date} has already been booked for this room!')

        return super(BookingForm, self).clean()

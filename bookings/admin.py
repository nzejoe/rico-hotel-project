from django.contrib import admin

from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    madel = Booking
    list_display = ['room', 'start_date', 'duration' ,'end_date', 'customer', 'status']

admin.site.register(Booking, BookingAdmin)
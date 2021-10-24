from django.contrib import admin

from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    madel = Booking
    list_display = ['room_id', 'start_date', 'end_date', 'customer_id', 'status']

admin.site.register(Booking, BookingAdmin)
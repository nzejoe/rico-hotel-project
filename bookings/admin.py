from django.contrib import admin
from django.db.models import fields

from .models import BookedRoom, Booking, BookingDetail, Payment

class BookingAdmin(admin.ModelAdmin):
    madel = Booking
    list_display = ['room', 'start_date', 'duration' ,'end_date', 'customer', 'status']

class BookingDetailInline(admin.TabularInline):
    model = BookedRoom
    extra = 0
    readonly_fields = ['room', 'customer', 'start_date', 'end_date', 'cost', 'duration', 'total_cost']

class BookingDetailAdmin(admin.ModelAdmin):
    model = BookingDetail
    list_display = ['customer', 'created']
    inlines = [BookingDetailInline, ]

admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingDetail, BookingDetailAdmin)
admin.site.register(Payment)

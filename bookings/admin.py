from django.contrib import admin

from .models import BookedRoom, Booking, BookingDetail

class BookingAdmin(admin.ModelAdmin):
    madel = Booking
    list_display = ['room', 'start_date', 'duration' ,'end_date', 'customer', 'status']

class BookingDetailInline(admin.TabularInline):
    model = BookedRoom
    extra = 0
    readonly_fields = ['created', 'room', 'customer', 'start_date', 'duration', 'end_date']

class BookingDetailAdmin(admin.ModelAdmin):
    model = BookingDetail
    list_dispay = ['room', 'customer']
    inlines = [BookingDetailInline, ]

admin.site.register(Booking, BookingAdmin)
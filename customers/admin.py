from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['first_name', 'email']
    fieldsets = (
        ('Login', {'fields': ['account']}),
        ('Personal', {'fields': ['first_name', 'middle_name', 'last_name', 'gender']}), 
        ('Contacts', {'fields': ['email', 'phone']}), 
        ('Address', {'fields': ['address_1', 'address_2', 'city', 'state', 'country']}),
        ('VIP', {'fields': ['is_vip']}),
        )


admin.site.register(Customer, CustomerAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


Account = get_user_model()
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ['username', 'email', 'is_active', 'is_staff']
    list_filter = ['username', 'email']
    fieldsets = ()
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)

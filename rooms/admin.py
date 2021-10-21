from django.contrib import admin

from .models import Room, RoomType


class RoomTypeAdmin(admin.ModelAdmin):
    model = RoomType
    list_display = ['name', 'price']


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ['room_number', 'room_type', 'room_type']


admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
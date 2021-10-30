import datetime
from django.shortcuts import render
from django.views import generic

#utils
from utils.bookings import get_booked_dates

from .models import Room
from bookings.models import BookedRoom


class RoomList(generic.ListView):
    model = Room
    template_name = 'room/room_list.html'
    context_object_name = 'rooms'


class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'room/room_detail.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        this_room = self.get_object()  # get this room's instance
        this_room_bookings = BookedRoom.objects.all().filter(room=this_room)  # check if room is been booked
        booked_dates = get_booked_dates(this_room_bookings)

        context = super(RoomDetail, self).get_context_data(**kwargs) # get context object
        context['booked_dates'] = booked_dates # add booked dates to context
        return context

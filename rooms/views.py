import datetime
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator

#utils
from utils.bookings import get_booked_dates

from .models import Room
from bookings.models import BookedRoom


def room_list(request):
     rooms = Room.objects.all().order_by('room_number')
     paginator = Paginator(rooms, 8)
     page = request.GET.get('page')
     page_room_list = paginator.get_page(page)
     
     context = {
         'rooms': page_room_list
     }
     return render(request, 'room/room_list.html', context)


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

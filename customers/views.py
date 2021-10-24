import datetime

from django.shortcuts import redirect, render
from django.urls import reverse

from bookings.models import Booking
from bookings.forms import BookingForm
from rooms.models import Room


def my_bookings(request):
    current_customer = request.user.customer.customer_id
    bookings = Booking.objects.filter(customer_id=current_customer)

    context = {
        'bookings': bookings
    }
    return render(request, 'customer/bookings.html', context)


def book_room(request, slug):
    room = Room.objects.get(slug=slug)
    current_customer = request.user.customer

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
        
            start_date = form.cleaned_data.get('start_date')
            duration = int(form.cleaned_data.get('duration'))
            end_date = datetime.timedelta(days=duration) + start_date

            booking = Booking.objects.create(
                room=room,
                customer=current_customer,
                start_date=start_date,
                duration=duration,
                end_date=end_date
            )

            booking.save()

            return redirect(reverse('my_bookings'))
    else:
        form = BookingForm()
    
    context = {
        'form': form,
        'room': room,
    }

    return render(request, 'customer/book_room.html', context)

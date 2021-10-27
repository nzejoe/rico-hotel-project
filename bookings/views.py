import datetime
import json
from django.contrib.admin.sites import site

from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from .models import Booking, Payment, BookingDetail, BookedRoom
from .forms import BookingForm
from rooms.models import Room
from customers.models import Customer


def my_bookings(request, total_cost=0):
    current_customer = request.user.customer
    bookings = Booking.objects.filter(customer=current_customer, status='Pending')
    for booking in bookings:
        total_cost += booking.duration * booking.room.room_type.price

    context = {
        'bookings': bookings,
        'total_cost': total_cost,
        'domain': get_current_site(request)
    }
    return render(request, 'booking/bookings.html', context)


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

    return render(request, 'booking/book_room.html', context)


def payment(request, total_cost=0):
    if request.body:
        data = json.loads(request.body)
        current_customer = Customer.objects.get(customer_id=request.user.customer.customer_id)
        bookings = Booking.objects.filter(customer=current_customer, status='Pending')

        print(current_customer.first_name)
        payment = Payment(
            payment_id = data.get('transID'),
            customer = current_customer,
            amount = data.get('amount'),
            payment_method = data.get('paymentMethod'),
            status = data.get('status'),
            created = data.get('created'),
        )

        payment.save()

        booking_detail = BookingDetail()
        booking_detail.customer = current_customer
        booking_detail.payment = payment
        booking_detail.total_book = len(bookings)

        booking_detail.save()

        for booking in bookings:
            total_cost += booking.duration * booking.room.room_type.price
            booking.status = 'Confirmed'
            booking.save()

            booked_room = BookedRoom()
            booked_room.booking_detail = booking_detail
            booked_room.customer = current_customer
            booked_room.room = booking.room
            booked_room.cost = booking.room.room_type.price
            booked_room.total_cost = total_cost
            booked_room.start_date = booking.start_date
            booked_room.duration = booking.duration
            booked_room.end_date = booking.end_date
            booked_room.save()
    else:
        pass

    return render(request, 'booking/payment.html')

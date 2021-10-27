import uuid

from django.db import models
from django.core.validators import MinValueValidator

from customers.models import Customer
from rooms.models import Room


class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    )
    booking_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='booking')
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(default=1, validators=(MinValueValidator(1),))
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.room.room_number


class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='payment')
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created = models.DateTimeField()

    def __str__(self):
        return self.customer.get_full_name()


class BookingDetail(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='booking_detail')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    total_book = models.IntegerField()
    is_booked = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.get_full_name()


class BookedRoom(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    booking_detail = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='booked_room')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    total_cost = models.DecimalField(decimal_places=2, max_digits=20)
    start_date = models.DateField()
    duration = models.IntegerField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room.room_number

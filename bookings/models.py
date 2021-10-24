import uuid

from django.db import models

from customers.models import Customer
from rooms.models import Room


class Booking(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    )
    booking_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking')
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='booking')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.room_id.room_number
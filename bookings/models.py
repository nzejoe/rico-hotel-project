import uuid

from django.db import models
from django.core.validators import MinValueValidator

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
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='booking')
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(default=1, validators=(MinValueValidator(1),))
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.room.room_number
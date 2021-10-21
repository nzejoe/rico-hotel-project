import uuid

from django.db import models
from django.urls import reverse

class RoomType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=19)


    def __str__(self):
        return self.name

class Room(models.Model):
    TYPE = (
        ('', 'Choose Type'),
        ('executive', 'Executive'),
        ('suite', 'Suite'),
    )

    FLOOR = (
        ('', 'Choose'),
        ('ground floor', 'Ground Floor'),
        ('first floor', 'First Floor'),
    )

    room_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    photo = models.ImageField(upload_to='rooms', null=True, blank=True)
    room_number = models.CharField(max_length=20)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    person_capacity = models.IntegerField()
    floor = models.CharField(max_length=20, choices=FLOOR, default='Choose')
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.room_number
    

    


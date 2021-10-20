import uuid

from django.db import models
from django.urls import reverse


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

    photo = models.ImageField(upload_to='rooms')
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=30, choices=TYPE, default='Choose Type')
    person_capacity = models.IntegerField()
    floor = models.CharField(max_length=20, choices=FLOOR, default='Choose')
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})
    

    


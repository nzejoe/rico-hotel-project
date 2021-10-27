import uuid

from django.db import models
from accounts.models import Account


class Customer(models.Model):
    GENDER = (
        ('', 'Choose gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    customer_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    is_vip = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10, choices=GENDER, default='Choose gender')
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

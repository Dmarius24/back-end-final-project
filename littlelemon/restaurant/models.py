from django.db import models
from rest_framework import viewsets

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(null=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} : {str(self.bookingdate)}'



class SingleMenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class BookingViewSet(models.Model):
    items = Booking.objects.all()
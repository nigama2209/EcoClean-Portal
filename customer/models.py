from django.db import models
from django.utils import timezone

class Cart(models.Model):
    bookingid = models.CharField(max_length=8, primary_key=True)   # Primary key
    servicename = models.CharField(max_length=25)
    typeofcloth = models.CharField(max_length=40)
    nopieces = models.IntegerField()
    price = models.IntegerField()
    username = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.username} - {self.servicename}"


class Booking(models.Model):
    bookingid = models.CharField(max_length=8, primary_key=True)
    username = models.CharField(max_length=40)
    paymentdetails = models.CharField(max_length=20)
    totalamount = models.IntegerField()
    bookingdate = models.DateField(default=timezone.now)
    cartitems = models.ManyToManyField('Cart', blank=True)  # ManyToManyField for cart items

    def __str__(self):
        return f"Booking {self.bookingid} - {self.username}"



class Feedback(models.Model):
    bookingid = models.CharField(max_length=8)   # not primary here, multiple feedbacks per booking possible
    username = models.CharField(max_length=40)
    rating = models.IntegerField()
    message = models.CharField(max_length=220)

    def __str__(self):
        return f"Feedback by {self.username} on {self.bookingid}"

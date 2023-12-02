

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# City Model
class City(models.Model):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name

# Club Model
class Club(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):

    city = models.ForeignKey(City, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

# UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields if necessary

    def __str__(self):
        return self.user.username

# Review Model

# MongoDB
class Review(models.Model):
    club = models.CharField(max_length=255)
    rating = models.IntegerField()

    class Meta:
        app_label = 'clubbing'  
        db_table = "ratings"

    def __str__(self):
        return f"{self.club} ({self.rating})"


# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    date_booked = models.DateTimeField()

    def __str__(self):
        return f"Booking by {self.user.user.username} for {self.event.name}"


from django.contrib import admin

# Register your models here.
from .models import City, Club, Event, UserProfile, Review, Booking

admin.site.register(City)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Review)


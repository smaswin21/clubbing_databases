from django.contrib import admin
# Importing the admin module:
# Register your models here.
from .models import City, Club, Event, UserProfile, Review, Booking

# Registering models with the admin site

""" 

Each admin.site.register() call registers a specific model with the Django admin site. 
This allows you to manage instances of that model through the admin interface. 
For example, registering the City model allows you to create, edit, and delete city records.

"""

admin.site.register(City)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Review)


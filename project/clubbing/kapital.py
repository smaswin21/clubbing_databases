import os
import django
from bs4 import BeautifulSoup

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from clubbing.models import City, Club  # Replace 'your_app' with the actual app name

# Function to extract club information remains the same

# The city "Madrid" is already in your database
city = City.objects.get(city_name='Madrid')

# The extracted club information
club_info = {
    'Name': 'Kapital',
    'Address': 'Calle de Atocha, 125, 28012 Madrid, Spain',  
    'Contact info': '+34 914 20 29 06',  
    'Type': 'Nightclub', 
    'Times': 'Wed - Sun: 11 pm - 6 am' 
}

# Create or update the Club instance
club, created = Club.objects.update_or_create(
    name=club_info['Name'],
    defaults={
        'city': city,
        'address': club_info['Address'],
        'contact_info': club_info['Contact info'],
        'type': club_info['Type']
    }
)

if created:
    print(f"Club {club.name} created successfully with id {club.id}")
else:
    print(f"Club {club.name} already exists or updated.")


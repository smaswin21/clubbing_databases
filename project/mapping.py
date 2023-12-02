import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from clubbing.models import City, Club  # Replace 'clubbing' with your actual app name

def save_club_to_database(club_data):
    # Create or get the city instance
    city_name = "Madrid"  # Adjust city name as needed
    city, created = City.objects.get_or_create(city_name=city_name)  # Use 'city_name' instead of 'name'

    # Create or update the club instance
    club, created = Club.objects.update_or_create(
        name=club_data['Name'],
        defaults={
            'city': city,
            'address': club_data.get('Address', 'Address not provided'),
            'contact_info': club_data.get('Contact info', 'Contact info not provided'),
            'type': club_data.get('Type', 'Type not provided')  # Ensure your model has 'type' field
            # Add other fields as needed
        }
    )
    return club

# Extracted clubs data
extracted_clubs = [
    {'Name': 'Goya Social Club', 'Address': 'Calle', 'Contact info': 'Fax--', 'Type': 'TimesFri - Sat: 12am - 6am', 'times': 'Fri - Sat: 12am - 6am'},
    {'Name': 'Panda Club', 'Address': 'Calle', 'Contact info': 'Fax--', 'Type': 'TimesCheck official website and social media.', 'times': ''},
    {'Name': 'Icon Club', 'Address': 'Not Found', 'Contact info': 'Not Found', 'Type': 'Not Found', 'times': 'Not Found'},
    {'Name': 'Lab Club', 'Address': 'Calle', 'Contact info': 'Fax--', 'Type': 'TimesMon, Wed, Fri and Sat: Midnight - 6amThurs: 10pm - 4.30amConsult full programme on the official website.', 'times': 'Mon, Wed, Fri and Sat: Midnight - 6am'},
    {'Name': 'Panda', 'Address': 'Calle', 'Contact info': 'Fax--', 'Type': 'TimesCheck official website and social media.', 'times': ''},
    {'Name': 'Commo', 'Address': 'Not Found', 'Contact info': 'Not Found', 'Type': 'Not Found', 'times': 'Not Found'},
    {'Name': 'Sala', 'Address': 'Calle', 'Contact info': 'Fax--', 'Type': 'TimesWed - Sat and Holidays: 12am - 6am', 'times': 'Wed - Sat and Holidays: 12am - 6am'}
]

# Save each club to the database
for club_data in extracted_clubs:
    club = save_club_to_database(club_data)
    print(f"Club {club.name} saved or updated successfully with id {club.id}")

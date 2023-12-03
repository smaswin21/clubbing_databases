import os
import django
import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from clubbing.models import Event, City  # Assuming you have a City model

# Helper function to parse the date and time string into a datetime object
def parse_date_time(date_time_str):
    start_date_time_str = date_time_str.split('-')[0].strip().replace('\t', ' ')
    return datetime.datetime.strptime(start_date_time_str, '%a, %d %b %Y %H:%M')

# Ensure 'Madrid' is in the City model, otherwise create it
madrid, created = City.objects.get_or_create(city_name='Madrid')

# Your scraped events data
events_data = [
    ('FUCKING MONDAY', 'Mon, 27 Nov 2023 23:30 - Tue, 28 Nov 2023 05:30', ['Smart casual', 'Commercial', 'Reggaeton', 'Electronic']),
    ('TEATRO KAPITAL - THURSDAY', 'Thu, 30 Nov 2023 23:00 - Fri, 01 Dec 2023 05:30', ['Commercial music']),
    ('BACK TO ICON', 'Thu, 14 Dec 2023 23:59 - Fri, 15 Dec 2023 05:30', ['Commercial music mix']),
    ('TOY ROOM FRIDAYS', 'Fri, 08 Dec 2023 23:59 - Sat, 09 Dec 2023 06:00', ['+21', 'Smart casual', 'Commercial', 'Hip hop', 'Reggaeton', 'Electronic']),
    ('FRIDAY PUBCRAWL', 'Fri, 24 Nov 2023 23:00 - Sat, 25 Nov 2023 06:00', ['Commercial music mix']),
]

# Loop over the events and add them to the database
for city_name, date_time_str, music_types in events_data:
    date_time = parse_date_time(date_time_str)
    
    # Create and save the new Event object
    event, created = Event.objects.get_or_create(
        name=city_name,
        city=madrid,
        defaults={
            'date_time': date_time,
            'description': ', '.join(music_types)
        }
    )
    
    if created:
        print(f'Event "{city_name}" created with date and time {date_time}.')
    else:
        print(f'Event "{city_name}" already exists.')

print('All events processed.')

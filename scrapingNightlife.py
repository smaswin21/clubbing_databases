import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

# 1 - Fucking Monday 
# Load the HTML content from the uploaded file
file_path = "Clubs_Scraping/FUCKING MONDAY.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

# Find the event details container
event_details = soup.find('div', class_='event-details')

# Extract the title, date and time, and music types
title = event_details.find('h1', itemprop='name').get_text(strip=True)
date_time = event_details.find('h6', itemprop='date').get_text(strip=True)
music_types = [li.get_text(strip=True) for li in event_details.find('div', class_='tags tags-left').find_all('li')]

print((title, date_time, music_types))

# 2 - Teatro Kapital
file_path2 = "Clubs_Scraping/TEATROKAPITAL.html"
with open(file_path2, 'r', encoding='utf-8') as file:
    html_content2 = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content2, 'lxml')

# Find the event details container
event_details = soup.find('div', class_='event-details')

# Extract the title, date and time, and music types
title = event_details.find('h1', itemprop='name').get_text(strip=True)
date_time = event_details.find('h6', itemprop='date').get_text(strip=True)
music_types = [li.get_text(strip=True) for li in event_details.find('div', class_='tags tags-left').find_all('li')]

print((title, date_time, music_types))

# 3 - Icon
file_path3 = "Clubs_Scraping/ICON.html"
with open(file_path3, 'r', encoding='utf-8') as file:
    html_content3 = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content3, 'lxml')
# Find the event details container
event_details = soup.find('div', class_='event-details')
# Extract the title, date and time, and music types
title = event_details.find('h1', itemprop='name').get_text(strip=True)
date_time = event_details.find('h6', itemprop='date').get_text(strip=True)
music_types = [li.get_text(strip=True) for li in event_details.find('div', class_='tags tags-left').find_all('li')]

print((title, date_time, music_types))

# 4 - Toy Room

file_path4 = "Clubs_Scraping/toyroom.html"
with open(file_path4, 'r', encoding='utf-8') as file:
    html_content4 = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content4, 'lxml')
# Find the event details container
event_details = soup.find('div', class_='event-details')
# Extract the title, date and time, and music types
title = event_details.find('h1', itemprop='name').get_text(strip=True)
date_time = event_details.find('h6', itemprop='date').get_text(strip=True)
music_types = [li.get_text(strip=True) for li in event_details.find('div', class_='tags tags-left').find_all('li')]

print((title, date_time, music_types))

# 4 - Commo

file_path5 = "Clubs_Scraping/commo.html"
with open(file_path5, 'r', encoding='utf-8') as file:
    html_content5 = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content5, 'lxml')
# Find the event details container
event_details = soup.find('div', class_='event-details')
# Extract the title, date and time, and music types
title = event_details.find('h1', itemprop='name').get_text(strip=True)
date_time = event_details.find('h6', itemprop='date').get_text(strip=True)
music_types = [li.get_text(strip=True) for li in event_details.find('div', class_='tags tags-left').find_all('li')]

print((title, date_time, music_types))




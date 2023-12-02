import sys
from bs4 import BeautifulSoup

def scrape_club_info(file_path, club_name):
    # Read the HTML content
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Scraping relevant information
    club_info = {
        'Name': club_name,
        'Address': soup.find(text='Address').find_next().get_text(strip=True) if soup.find(text='Address') else 'Not Found',
        'Contact info': soup.find(text='Telephone').find_next().get_text(strip=True) if soup.find(text='Telephone') else 'Not Found',
        'Type': soup.find(text='Type').find_next().get_text(strip=True) if soup.find(text='Type') else 'Not Found',
        'times': soup.find(text='Times').find_next().get_text(strip=True) if soup.find(text='Times') else 'Not Found',
    }
    return club_info

# Scraping Done for - Kapital, Fabrik, Goya
# Paths to HTML files

file_paths = [
    ('Clubs_Scraping/goya.html', 'Goya Social Club'),
    ('Clubs_Scraping/panda.html', 'Panda Club'),
    ('Clubs_Scraping/ICON.html', 'Icon Club'),  # Fixed comma here
    ('Clubs_Scraping/Lab.html', 'Lab Club'),    # Fixed comma here
    ('Clubs_Scraping/panda.html', 'Panda'),     # Fixed comma here
    ('Clubs_Scraping/commo.html', 'Commo'),
    ('Clubs_Scraping/sala.html', 'Sala'),
]

# Scraping information for each club
clubs_data = [scrape_club_info(path, name) for path, name in file_paths]

# Printing the scraped information
for club in clubs_data:
    print(club)


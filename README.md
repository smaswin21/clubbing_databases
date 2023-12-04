# Clubbing in Madrid: A Comprehensive Guide to the City's Nightlife 🌃💃

## 🌟 Project Overview
This project, developed by us, is a comprehensive guide to the vibrant clubbing scene in Madrid. It offers detailed insights into various clubs, events, and nightlife experiences in the city, making it an essential resource for party-goers and nightlife enthusiasts.

### Key Features:
- 🎉 Detailed information on popular clubs in Madrid.
- 📅 Event listings and schedules for major nightlife events.
- 📍 Interactive mapping of club locations and events.
- 📝 User reviews and ratings for clubs and events.

### 💡 Data Collection and Analysis
The project leverages web scraping and database management to gather and present information:

- **Web Scraping**: Extracts data from club websites to compile comprehensive club listings.
- **Database Management**: Organizes and stores club and event data for easy retrieval and analysis.
- **User Review System**: Allows users to post reviews and ratings, providing valuable insights into each club's experience.

### ✨ Future Enhancements
The project is open to future enhancements to enrich the user experience:

- **Mobile App Integration**: Develop a mobile application for easier access and real-time updates.
- **Social Features**: Implement social networking features to connect club-goers and share experiences.
- **Advanced Filtering Options**: Provide more detailed search and filter options for users to find clubs and events that match their preferences.
- **Live Event Updates**: Integrate live updates for events, including ticket availability and special announcements.

## 🛠 Tech Stack
- Python: For web scraping and backend development.
- Django: A high-level Python web framework for rapid development.
- MongoDB: A NoSQL database for storing and managing club and event data.
- Djongo: A connector for using Django with MongoDB.

## 🛠 Installation and Setup Guide

### Prerequisites
- Python
- pip
- virtualenv
- MongoDB
- BeautifulSoup (Web-Scraping)

### Step-by-Step Installation

1. **Install MongoDB**:
   - Follow the instructions on the [MongoDB website](https://www.mongodb.com/try/download/community) to install MongoDB on your system.

2. **Install pymongo and Djongo**:

   pip install pymongo
   
   pip install Django djongo


3. **Install Virtual Environment**:

   pip install virtualenv

   virtualenv venv

   Windows

   venv\Scripts\activate

   MacOS

   source venv/bin/activate


4. **Install Required Packages**:

   pip install wheel

   pip install django

   
   pip install django
   
   pip install mysqlclient

5. **Create Database Tables**:

   python manage.py makemigrations

   python manage.py migrate

6. **Run the Server**:


   python manage.py runserver 

   python manage.py runserver

Now, you should be able to access the application at `http://localhost:8000`.

This will initiate the web scraping process and populate the database with the latest clubbing information.



## 📁 Project Structure

databases_project/
├── Clubs_Scraping/
│   ├── Various HTML files for club data
├── project/
│   ├── clubbing/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── manage.py
│   ├── ...
├── scrapingMadrid.py
├── scrapingNightlife.py
└── segovia.sql


## 🚀 Usage

This section includes images for our project.

<img width="1505" alt="Screenshot 2023-12-04 at 23 11 23" src="https://github.com/smaswin21/clubbing_databases/assets/130904493/b92b0c35-2a52-44e8-a587-1795096e6f47">

<img width="1189" alt="Screenshot 2023-12-04 at 23 11 09" src="https://github.com/smaswin21/clubbing_databases/assets/130904493/6f4328e8-982c-47ef-941e-9298f7dd788b">

<img width="1194" alt="Screenshot 2023-12-04 at 22 45 22" src="https://github.com/smaswin21/clubbing_databases/assets/130904493/cc3e23e9-e2f9-4a1c-a7a7-c17698cd89f8">

<img width="1502" alt="Screenshot 2023-12-04 at 22 45 10" src="https://github.com/smaswin21/clubbing_databases/assets/130904493/f7d463db-cf8c-47f6-85a9-234ce310674e">


## 👥 Contributing
Contributions are welcome! If you have suggestions or find a bug, please open an issue or submit a pull request.


Dive into the heart of Madrid's nightlife with this comprehensive guide. Discover the best clubs, events, and experiences the city has to offer! 🎶🌆

[GitHub Repository](https://github.com/smaswin21/databases_project)


   

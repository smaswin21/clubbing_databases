import os
import django
from pymongo import MongoClient

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from clubbing.models import Review, Club  # Replace 'your_app_name' with the name of your Django app

# Connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["clubs"]  # Replace with your actual MongoDB database name
reviews_collection = db["ratings"]  # Replace with your actual MongoDB collection name

# Fetch the reviews from MongoDB
mongo_reviews = list(reviews_collection.find({}))

# Update or create a review in Django for each document in the 'ratings' collection from MongoDB
for mongo_review in mongo_reviews:
    # Get or create the club instance from the 'Club' model
    club, club_created = Club.objects.get_or_create(name=mongo_review['club'])

    # Update or create the review in the 'Reviews' model
    review, review_created = Review.objects.update_or_create(
        club=club,
        defaults={'rating': mongo_review['rating']}
    )
    if review_created:
        print(f"Created new review for {club.name} with rating {mongo_review['rating']}")
    else:
        print(f"Updated review for {club.name} with rating {mongo_review['rating']}")

print('All reviews have been updated in Django.')

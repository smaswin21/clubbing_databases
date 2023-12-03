import pymongo

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["clubs"]  # Replace with your actual MongoDB database name
reviews_collection = db["ratings"]  # Replace with your actual MongoDB collection name

# List of clubs with assigned ratings
club_ratings = {
    "Liberty": 4.2,
    "Sala": 3.8,
    "Commo": 4.1,
    "Panda": 4.3,
    "Lab Club": 4.0,
    "Icon Club": 4.5,
    "Panda Club": 3.9,
    "Istar": 4.1,
    "La Luna": 3.7,
    "Sabat": 3.6,
    "Kotaho Clubs": 3.8,
    "La Mentira": 3.5,
    "Irish": 4.0,
    "Kapital": 4.6,
    "Fabrik": 4.7,
    "Goya Social Club": 4.4
}

# Update MongoDB with the assigned ratings
for club, rating in club_ratings.items():
    review_data = {
        "club": club,
        "rating": rating
    }
    reviews_collection.update_one(
        {"club": club},
        {"$set": review_data},
        upsert=True
    )

print("All reviews have been updated in MongoDB.")

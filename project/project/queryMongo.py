import pymongo

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["clubs"]  # Your MongoDB database name
reviews_collection = db["ratings"]  # Your MongoDB collection name

# Insert a review into the 'ratings' collection
review_data = {
    "club": "Goya Social Club",
    "rating": 5,
}
inserted_review = reviews_collection.insert_one(review_data)
print("Inserted document ID:", inserted_review.inserted_id)

# Retrieve a review from the 'ratings' collection
query = {"club": "Goya Social Club"}
retrieved_review = reviews_collection.find_one(query)
if retrieved_review:
    print("Retrieved document:", retrieved_review)
else:
    print("No document found.")
